import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request
import time

# GitHub Personal Access Token，替换为您的令牌

# 设置请求头，包含 Authorization 字段

page = 'page'
count = 0
# Get your cookie, otherwise the page information cannot be obtained
cookie = 'cpu_bucket=lg; preferred_color_mode=light; tz=Asia%2FShanghai; _device_id=620b4dd0c257eea68571dc9a4ab7b6cd; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=Menghua1; _octo=GH1.1.1764517066.1736214710; user_session=IpY7qtNxmay2gNsgIBtlTUCzmJyaRknk56qNQj7GY7mVInNn; __Host-user_session_same_site=IpY7qtNxmay2gNsgIBtlTUCzmJyaRknk56qNQj7GY7mVInNn; saved_user_sessions=111940661%3AIpY7qtNxmay2gNsgIBtlTUCzmJyaRknk56qNQj7GY7mVInNn; _gh_sess=8c8%2Bc0QSbayLy%2BGqDrpYiAK2AGgz2xJTH4DiyUNhmaz89VqRs66fojjnvMUs0FHNDmu%2FSZQD8YEYgW%2Fm61riyU%2BFC6HL%2Fzw%2FOTpnAnaQRiiHYWXiiPdiW11ziw%2BsnJ%2FQZskLTkmYRY1qcFhfRoIQVUfRVjBFZBjQ8w7sGMfbwYOE7r2KOJXarXXo%2Far8YhcVPT%2B2s002p0%2BXHZGv%2B26tLpjRP3mnCvmdZI8wbyEcR85LuUXsuQLgDuZ9E%2BUOKvOmVanhTkUabkvIObCaZAyWdJfhQdDh8YMLJL%2BnqUjMIzP14MhmbZNxTXj%2BdHWfYjTiDHpvV%2F%2Fdbkcyb4TahTVUxQVJ%2Brdk1OIeHA5tzMO9WJ3%2FFKvRvn0SQiwVw98hywBq83DjTAV797DYCoD2jfS%2Fz8CAEIg4sUjH8vwKyIbHCAfgs5Z7WndN8%2FssrF8SH8AHjZIzYTavzEg2IYrX3o7PBAVpEmKV5xyBqOXQDmyILulEnq1sIpQ46Vqxq4%2FqjJMCtbPU0CavEjIOsi%2F%2BuB9QXxZ8%2F0WVgJ3OwFK5R65SoIw357a5OS9Ew5aTQ%2FpcyNxw%2B9Jeyxaoiz2m%2BlQBZHkMKHncRyd2JudlxuTtBMVUx62F6Y%2BgVEk8ZrV2TlWZ3QQzuKrEw9MD5UXu2An8LB9J01uqYT6joVLB%2F8gHDSHR4gZTUYJG6BYqdKfP7OG2sTn2NC%2BjpYIDkaHpwtPpYbLjXbr%2F29VM4igTg28xynXPvt2MVHWhuM7%2B%2BMo7mVj0LwpaoZj5Q6vcASvbh0KN5zpmKHfyjeFW1PjW1lallzti8A%2BBpVA9gJuZfsXt4ctbMS%2FTjUm8CpPGVVQRzdEYCiDGUpqOfCpQXqjtk3JkyqKjPbuAI%2FpskWl6vRKvTx9ZRMEVG7y%2FPuc7m2Bmh22TUBWwZVLTExkBKFn0Y1AJPlidL3iJ%2FZe9Pz%2FA7XjAZUqjbVDV%2Bj21i1cj%2FU9CU7w%2FWCtDXOMHFgo%3D--2wrWj8RMrQOa6zxJ--R7JKabtn7M8zlwn4Ed8zSg%3D%3D'
headers = {
    'cookie': cookie                         # 如果需要，您可以保留 cookie
}

for i in range(1,101):
    page = f'page={i}'
    print(f"00000000000000000000000000000000000000page={page}")
    response = urllib.request.urlopen(Request('https://github.com/orgs/Azure-Samples/repositories?q=sort:name-asc&%s' % (page)))
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
                    with open('output.txt', 'a', encoding='utf-8') as file:
                        file.write(repo + '\n')
                    print(repo)
                    print(f"11111111111111111111111111Processing repository: {repo_name}")
                else:
                    print(f"Skipping repository {repo_name}, as 'setup-azd' is 0 or not found.")
                # Avoid too many request error.
                time.sleep(2) 
        print('------------------------------------'+page+',total count=%d'%(count))