import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request
import time

page = 'page'
count = 0
# Get your cookie, otherwise the page information cannot be obtained
cookie = ''
for i in range(1,2):
    page = 'page=%d'%(i)
    response = urllib.request.urlopen('https://github.com/orgs/Azure-Samples/repositories?q=sort:name-asc&%s'%(page))

    if response:
        # Get page content
        html_content = response.read().decode('utf-8')
        # Convert the obtained content into BeautifulSoup format and use html.parser as the parser
        soup = BeautifulSoup(html_content, 'html.parser')
        # Find all span tags
        all_span = soup.find_all('span', attrs={'class':'Text-sc-17v1xeu-0 gPDEWA'})
        for span in all_span:
            if(span.text != '•'):
                href = 'https://github.com/search?q=repo%3AAzure-Samples%2F'+(span.text)+'%20infra%2Fcore&type=code'
                r = urllib.request.urlopen(Request(url=href, headers={'cookie': cookie}))
                repo_html_content = r.read().decode('utf-8')
                repo_soup = BeautifulSoup(repo_html_content, 'html.parser')
                # print(repo_soup)
                find_infra_core = repo_soup.find('span', attrs={'class':'Text-sc-17v1xeu-0 gPDEWA'})
                if(find_infra_core.text != '0'):
                    repo = 'https://github.com/Azure-Samples/'+span.text
                    count+=1
                    with open('output.txt', 'a', encoding='utf-8') as file:
                        file.write(repo + '\n')
                    print(repo)
                # Avoid too many request error.
                time.sleep(1) 
        print('------------------------------------'+page+',total count=%d'%(count))
