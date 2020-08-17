import requests
from bs4 import BeautifulSoup
import pprint

# preparing data from MULTIPLE pages
#     sites = [f'https://news.ycombinator.com/news?p={page}' for page in range(1,20)]
#
#     responses = [requests.get(site) for site in sites]
#     soup = []
#     for idx, res in enumerate(responses):
#         #check the status code of response
#         if res.status_code == 200:
#             soup_item = BeautifulSoup(res.text, 'html.parser')
#             #check if page is not empty
#             if soup_item.find_all('athing', limit=1):
#                 soup.append(soup_item)
#
#
#     links = [soup[item].select('.storylink') for item in soup]
#     subtext = [soup[item].select('.subtext') for item in soup]

#preparing data from ONE page

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def creat_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'points': points})

    return sorted(hn, key=lambda i:i['points'], reverse=True)


result = creat_custom_hn(links, subtext)


pprint.pprint(result)

