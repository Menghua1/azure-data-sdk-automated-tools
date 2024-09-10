using Microsoft.VisualStudio.TestTools.UnitTesting;
using ContentValidationTool;
using HtmlAgilityPack;
using System.Text.RegularExpressions;

namespace ContentValidationTool.Tests;

[TestClass]
public class TestBrokenLink
{
    private readonly Validation _validation;
    private List<string> _testPages { get; set; }

    public TestBrokenLink(){
        _validation = new Validation();
        _testPages = _validation.Validate();
    }

    [TestMethod]
    [DynamicData(nameof(_testPages))]
    public void TestMethod1(string testPage)
    {
        bool result = String.IsNullOrEmpty(testPage);

        Assert.IsFalse(result);
    }

    [TestMethod]
    public void ValidateCrossLink()
    {
        string pageUri = "https://azuresdkdocs.blob.core.windows.net/$web/python/azure-mgmt-advisor/10.0.0b1/index.html";
        var web = new HtmlWeb();
        var doc = web.Load(pageUri);
        var failCount = 0;
        var failMsg = "";

        foreach (HtmlNode aNode in doc.DocumentNode.SelectNodes("//a"))
        {
            string content = aNode.InnerText;
            // Console.Write(link.Value + ": ");
            if (Regex.Replace(aNode.InnerText, @"\s", "") == "" || aNode.GetAttributeValue("title", "") == "Permalink to this headline" || aNode.GetAttributeValue("href", "") == "#")
            {
                continue;
            }

            string link = aNode.GetAttributeValue("href", "");

            var subContent = content.ToLower().Replace(".", " ").Split(" ");

            var tag = 0;

            foreach (string s in subContent)
            {
                if (link.ToLower().Replace(".", " ").Contains(s))
                {
                    tag = 1;
                    break;
                }
                else
                {
                    continue;
                }
            }

            if(tag == 0)
            {
                failCount++;
                failMsg = failMsg + content + ": " + link + "; ";
            }
        }

        Assert.IsTrue(failCount == 0, failMsg);
    }

    [TestMethod]
    public void ValidateDisplayLink()
    {
        string pageUri = "https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-inference/1.0.0b3/index.html#create-and-authenticate-a-client-directly-using-key";
        var web = new HtmlWeb();
        var doc = web.Load(pageUri);
        var errorList = new List<string>();
        var codeBlocks = doc.DocumentNode.SelectNodes("//div[contains(@class, 'notranslate')]");
        if (codeBlocks != null)
        {
            foreach (var item in codeBlocks)
            {
                if (item.Attributes["class"].Value.Contains("highlight-bash"))
                {
                    if (item.InnerText.StartsWith(" "))
                    {
                        errorList.Add(item.InnerText);
                    }
                }
                else if (item.Attributes["class"].Value.Contains("highlight-python"))
                {
                    var text = item.InnerText;
                    // TODO, the page text somehow contains a extra new line at the end
                    // We need to confirm if it is common or not
                    Assert.IsFalse(true, "\n" + text);
                }
            }
        }
    }


    [TestMethod]
    public void selfTest()
    {
        var failCount = 0;

        var failMsg = "";

        string content = "azure.mgmt.advisor package";

        string link = "azure.mgmt.advisor.html";

        var subContent = content.ToLower().Replace(".", " ").Split(" ");

        var tag = 0;

        foreach (string s in subContent)
        {
            if (link.ToLower().Replace(".", " ").Contains(s))
            {
                tag = 1;
                break;
            }
            else
            {
                continue;
            }
        }

        if (tag == 0)
        {
            failCount++;
            failMsg = failMsg + content + ": " + link + "; ";
        }

        Assert.IsTrue(failCount == 0, failMsg);
    }
}