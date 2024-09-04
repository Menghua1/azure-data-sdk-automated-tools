using HtmlAgilityPack;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Text;
using System.Text.RegularExpressions;
using System.Xml.Linq;

// Get All Service Name from CSV file.
List<string> serviceNames = GetAllService();

// Load all service.html pages, such as https://azure.github.io/azure-sdk-for-python/advisor.html.
serviceNames.ForEach(item =>
{
    string servicePageLink = GetServicePages(item);
    List<string> pkgVersionPages = GetPackVersionPages(servicePageLink);

    pkgVersionPages.ForEach(item =>
    {
        Console.WriteLine(item);
    });
});
// string servicePageLink = GetServicePages("Advisor");
// GetPackVersionPages(servicePageLink);

List<string> GetAllService()
{
    StreamReader reader = new StreamReader("D:\\data\\repo\\azure-data-sdk-automated-tools\\ContentValidationTool\\ConsoleApp1\\testgithubioservices.csv");
    string line = "";
    List<string> list = new List<string>();

    // Remove the first line. So read twice.
    line = reader.ReadLine();
    line = reader.ReadLine();

    while (line != null)
    {
        list.Add(line);
        line = reader.ReadLine();
    }

    return list;
}

string GetServicePages(string serviceName)
{
    // Process the serviceName string, convert it to all lowercase and delete all spaces.
    serviceName = serviceName.ToLower().Replace(" ", "");

    // Splicing service page link.
    string servicePageLink = $"https://azure.github.io/azure-sdk-for-python/{serviceName}.html";
    
    return servicePageLink;
}

List<string> GetPackVersionPages(string servicePageLink)
{
    List<string> pkgVersionPages = new List<string>();
    // Console.WriteLine(servicePageLink);
    HtmlWeb web = new HtmlWeb();
    var doc = web.Load(servicePageLink);
    HtmlNodeCollection pkgNames = doc.DocumentNode.SelectNodes("//h4");
    foreach (var pkgName in pkgNames)
    {
        // Splice to get the pkg version url.
        var pkgVersionRequestLink = $"https://azuresdkdocs.blob.core.windows.net/$web/python/{pkgName.InnerText}/versioning/latest-preview";
        var pkgVersion = GetPackLatestPreVersion(pkgVersionRequestLink);
        var pkgVersionPage = $"https://azuresdkdocs.blob.core.windows.net/$web/python/{pkgName.InnerText}/{pkgVersion}/index.html";

        pkgVersionPages.Add(pkgVersionPage);
    }
    return pkgVersionPages;
}

string GetPackLatestPreVersion(string pkgVersionRequestLink)
{
    ServicePointManager.Expect100Continue = true;
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
    CookieContainer cookies = new CookieContainer();
    var request = (HttpWebRequest)WebRequest.Create(pkgVersionRequestLink);
    request.CookieContainer = cookies;
    request.Method = "GET";
    request.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36";
    request.ContentType = "application/json";
    request.Headers.Add("accept-language", "en,hr;q=0.9");
    request.Headers.Add("accept-encoding", "");
    request.Headers.Add("Upgrade-Insecure-Requests", "1");
    WebResponse response = request.GetResponse();
    StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
    string responseFromServer = reader.ReadToEnd();
    reader.Close();
    response.Close();

    return responseFromServer;
}

void GetAllHref()
{
    // foreach (HtmlNode aNode in htmlDoc.DocumentNode.SelectNodes("//a"))
    // {
    //     // Console.Write(link.Value + ": ");
    //     if (Regex.Replace(aNode.InnerText, @"\s", "") != "" && aNode.GetAttributeValue("title", "") != "Permalink to this headline")
    //     {
    //         Console.Write(aNode.InnerText + ": ");
    //     }
    //     else
    //     {
    //         continue;
    //     }

    //     string att = aNode.GetAttributeValue("href", "");
    //     Console.WriteLine(att);
    // }
}

