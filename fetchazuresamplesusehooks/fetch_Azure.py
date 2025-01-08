import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request
import time

# GitHub Personal Access Token，替换为您的令牌

# 设置请求头，包含 Authorization 字段

page = 'page'
count = 0
# Get your cookie, otherwise the page information cannot be obtained
cookie = ''
headers = {
    'cookie': cookie                         # 如果需要，您可以保留 cookie
}

for i in range(35,101):
    page = f'page={i}'
    print(f"00000000000000000000000000000000000000page={page}")
    response = urllib.request.urlopen(Request('https://github.com/orgs/Azure/repositories?q=sort:name-asc&%s' % (page)))
    print(f'https://github.com/orgs/Azure-Samples/repositories?q=sort:name-asc&{page}')
    if response:
        # Get page content
        html_content = response.read().decode('utf-8')
        # Convert the obtained content into BeautifulSoup format and use html.parser as the parser
        soup = BeautifulSoup(html_content, 'html.parser')
        # Find all span tags
        all_span = soup.find_all('span', attrs={'class':'Text__StyledText-sc-17v1xeu-0 hWqAbU'})
        print(f"Found {len(all_span)} span elements with the specified class.")
        for span in all_span:
            repo_name = span.text.strip() 
            if(repo_name != '•'):
                encoded_repo_name = urllib.parse.quote(span.text.strip())
                print(f"222222222222222222222: {encoded_repo_name}")
                href = f'https://github.com/search?q=repo%3AAzure-Samples%2F{encoded_repo_name}%20setup-azd%40v1.0.0&type=code'
                r = urllib.request.urlopen(Request(url=href, headers=headers))
                repo_html_content = r.read().decode('utf-8')
                repo_soup = BeautifulSoup(repo_html_content, 'html.parser')
                # print(repo_soup)
                find_infra_core = repo_soup.find('span', attrs={'class':'Text__StyledText-sc-17v1xeu-0 hWqAbU'})
                print(f"333333333333333333333: {find_infra_core}")
                if find_infra_core and find_infra_core.text != '0':
                    repo = f'https://github.com/Azure-Samples/{span.text}'
                    count += 1
                    with open('output_all_Azure.txt', 'a', encoding='utf-8') as file:
                        file.write(repo + '\n')
                    print(repo)
                    print(f"11111111111111111111111111Processing repository: {repo_name}")
                else:
                    print(f"Skipping repository {repo_name}, as 'setup-azd' is 0 or not found.")
                # Avoid too many request error.
                time.sleep(2) 
        print('------------------------------------'+page+',total count=%d'%(count))