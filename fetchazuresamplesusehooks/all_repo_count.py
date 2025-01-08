import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request

# 设置请求头，如果需要，可以添加 Cookie 或其他字段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

def get_total_repositories():
    base_url = 'https://github.com/orgs/Azure-Samples/repositories?q=sort:name-asc'
    page = 1
    total_count = 0

    while True:
        url = f"{base_url}&page={page}"
        print(f"Fetching: {url}")

        # 创建请求对象
        request = Request(url, headers=headers)

        try:
            # 发送请求并获取响应
            response = urllib.request.urlopen(request)
            html_content = response.read().decode('utf-8')

            # 使用 BeautifulSoup 解析 HTML 内容
            soup = BeautifulSoup(html_content, 'html.parser')

            # 查找页面上的所有符合条件的 span 标签
            all_span = soup.find_all('span', attrs={'class': 'Text__StyledText-sc-17v1xeu-0 hWqAbU'})

            # 如果本页没有找到任何 span，说明已经到最后一页
            if not all_span:
                break

            # 累加仓库数量
            total_count += len(all_span)
            print(f"Page {page}: Found {len(all_span)} repositories")

            # 进入下一页
            page += 1
            
        except Exception as e:
            print(f"Error occurred: {e}")
            break

    return total_count

if __name__ == "__main__":
    total_repositories = get_total_repositories()
    print(f"Total repositories: {total_repositories}")
