import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

cookie = 'MicrosoftApplicationsTelemetryDeviceId=68d7a888-cb92-46b8-9a7f-341872857e4f; MSFPC=GUID=404e13d068d14906a111e960d1fe145f&HASH=404e&LV=202203&V=4&LU=1648173746439; _gid=GA1.3.1935413108.1724144902; _ga_V9ZJ8XJ34R=GS1.1.1724207630.15.1.1724208045.0.0.0; _ga_56W5K4ER5T=GS1.1.1724221320.6.1.1724221324.0.0.0; _ga=GA1.1.247573240.1635217871'

df = pd.read_csv('testgithubioservices.csv')
services = df['Service'].values.tolist()

pkgs = []
for service in services:
    service = service.replace(' ','').lower()
    print('service: %s'%(service))
    response = urllib.request.urlopen('https://azure.github.io/azure-sdk-for-python/%s.html'%(service))

    if response:
        html_content = response.read().decode('utf-8')
        # print(html_content)
        soup = BeautifulSoup(html_content, 'html.parser')
        packages = soup.find_all('h4')
        packages_str = ''
        for package in packages:
            packages_str = packages_str + package.text.strip() + ', '
        # print('packages: %s'%(packages_str))
        pkgs.append(packages_str)
        
a = [x for x in services]
b = [x for x in pkgs]

dataframe = pd.DataFrame({'Services': a, 'Packages': b})
dataframe.to_csv(r"testgithubio.csv", index=False)

        