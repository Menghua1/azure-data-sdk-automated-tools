import requests
from bs4 import BeautifulSoup
import time
import urllib.parse

# 设置请求头，包含 User-Agent 字段
cookie = ''
headers = {
    'cookie': cookie                         # 如果需要，您可以保留 cookie
}

# 基础搜索URL
base_search_url = 'https://github.com/search'

# 查询参数
query_params = {
    'q': 'org:Azure-Samples "setup-azd@v1.0.0"',
    'type': 'code',
    'p': 1  # 页码，从第1页开始
}

# 手动设置要搜索的页数
max_pages = 4  # 可以修改为任意需要搜索的页数

# 用于存储已找到的仓库
found_repos = set()

for page_num in range(1, max_pages + 1):
    # 构建当前页的搜索URL
    query_params['p'] = page_num
    search_url = f"{base_search_url}?{urllib.parse.urlencode(query_params)}"
    print(f"正在处理：{search_url}")

    # 发送HTTP GET请求
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print(f"无法获取页面内容，状态码：{response.status_code}")
        break

    # 解析页面内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有包含仓库名称的元素
    repo_elements = soup.find_all('div', class_='Box-sc-g0xbh4-0 kRFgrU search-title')
    print(f"找到 {len(repo_elements)} 个仓库")
    if not repo_elements:
        print("未找到更多的仓库，结束搜索。")
        break

    # 提取仓库名称并存储
    for repo_element in repo_elements:
        repo_name = repo_element.find('a')['href'].split(' ')[0]  # 获取仓库的 URL 部分
        if repo_name not in found_repos:
            found_repos.add(repo_name)
            repo_url = f"https://github.com/{repo_name}"
            print(f"找到仓库：{repo_url}")
            # 将结果写入文件
            with open('output.txt', 'a', encoding='utf-8') as file:
                file.write(repo_url + '\n')
        #不去重的
        # for repo_element in repo_elements:
        # repo_name = repo_element.find('a')['href'].split(' ')[0]  # 获取仓库的 URL 部分
        # repo_url = f"https://github.com/{repo_name}"
        # print(f"找到仓库：{repo_url}")
        # # 将结果写入文件
        # with open('output.txt', 'a', encoding='utf-8') as file:
        #     file.write(repo_url + '\n')

    # 为避免请求过于频繁，增加延时
    time.sleep(2)

# 输出搜索的页面数量
print(f"已搜索 {max_pages} 页")
