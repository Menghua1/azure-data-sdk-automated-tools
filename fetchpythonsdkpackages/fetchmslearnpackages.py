import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

# cookie = 'MicrosoftApplicationsTelemetryDeviceId=68d7a888-cb92-46b8-9a7f-341872857e4f; MSFPC=GUID=404e13d068d14906a111e960d1fe145f&HASH=404e&LV=202203&V=4&LU=1648173746439; _gid=GA1.3.1935413108.1724144902; _ga_V9ZJ8XJ34R=GS1.1.1724207630.15.1.1724208045.0.0.0; _ga_56W5K4ER5T=GS1.1.1724221320.6.1.1724221324.0.0.0; _ga=GA1.1.247573240.1635217871'

response = urllib.request.urlopen('https://learn.microsoft.com/en-us/python/api/overview/azure/?view=azure-python')

services = []
pkgs = []
if response:
    html_content = response.read().decode('utf-8')
    # print(html_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    all_services = soup.find_all('a', attrs={'data-linktype':'relative-path'})
    for service in all_services:
        services.append(service.text)
        href = 'https://learn.microsoft.com/en-us/python/api/overview/azure/'+ service['href']

        response_sub = urllib.request.urlopen(href)
        if response_sub:
            html_content_sub = response_sub.read().decode('utf-8')
            soup_sub = BeautifulSoup(html_content_sub, 'html.parser')
            all_packages = soup_sub.find_all('a', attrs={'data-linktype':'external'})
            packages_str = ''
            for package in all_packages:
                if(package.text != 'GitHub'):
                    packages_str = packages_str + package.text + ', '
            pkgs.append(packages_str)

a = [x for x in services]
b = [x for x in pkgs]

dataframe = pd.DataFrame({'Services': a, 'Packages': b})
dataframe.to_csv(r"testmslearn.csv", index=False)

        