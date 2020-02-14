import requests
from bs4 import BeautifulSoup
import pprint

pages = int(input("Enter the number of Hacker News pages to scrape: "))
res = []
for page in range(pages):
    res = requests.get('https://news.ycombinator.com/news' + '?p=' + str(page))
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    try:
        mega_links
    except NameError:
        mega_links = links
        mega_subtext = subtext
    else:
        mega_links += links
        mega_subtext += subtext


def create_custom_hn(mega_links, mega_subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].get_text()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].get_text().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda k: k['votes'], reverse=True)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
