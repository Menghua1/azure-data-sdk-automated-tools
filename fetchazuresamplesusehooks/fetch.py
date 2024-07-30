import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request
import time

page = 'page'
count = 0
# Get your cookie, otherwise the page information cannot be obtained
cookie = '_device_id=e740d20410241137525dd0d15d0a41e4; saved_user_sessions=81678720%3ABJRYOn9OKwMpT2AzoomgV7xgHXZKNujs1EEnGyJhbXyqwjG0; user_session=BJRYOn9OKwMpT2AzoomgV7xgHXZKNujs1EEnGyJhbXyqwjG0; __Host-user_session_same_site=BJRYOn9OKwMpT2AzoomgV7xgHXZKNujs1EEnGyJhbXyqwjG0; logged_in=yes; dotcom_user=zedy-wj; color_mode=%7B%22color_mode%22%3A%22dark%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark_dimmed%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; _octo=GH1.1.714910798.1721098088; _gh_sess=D9Pu2I%2B5Dk%2BKrgDYUTMMEZawXl1APnTJVqaX%2FKEZw6xW01NAK%2B1paSXjlmA9UtrHkb9x%2BLeFGDFW5x3v5Nxl84bFArM0QXYjQKn4eBvIDN2QyTypxxeEAyClenYEL48nk%2BHGlx2j%2BpV3Z1z45%2BzQqjZhicZfO0cwneH3LodLNFIgbberPera%2Fw8RtlYPeApnt%2FuTepn5BE2ppdtr0zkuNhLD8Lj2tu%2F5qUs00yAk3NfhiJPMHmoOZc80fxCaOoh33nN6aT%2BI2MPA4jHYyAWInPvrS0K3BqFy20M980%2FpRJ6pNt7nqXUpuCXlA00KhgjjN65RRRcdNdYWzmSV0kHiC%2BwSwHvIb5gQv70aXq44Jjx4zA3UqggPnHYbxep6BWocfzrFptHc0J%2B6yhE%2BLTj1H56lFifK9lncE3PpGnfxJA7nTI7jHYRRkdtfgxtCuICmoQKhu5YpDBAdWroTD%2BqeNU%2FVYN7OauD6eJsX6aN4MCQpdln%2F--VW%2FXkvvNaQzagZsw--EamEusPO1JnJaiKspKrOAA%3D%3D'
for i in range(1,89):
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
                href = 'https://github.com/search?q=repo%3AAzure-Samples%2F'+(span.text)+'%20Azure%2Fazure-dev%2Fmain%2Fschemas%2Fv1.0%2Fazure.yaml.json&type=code'
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
