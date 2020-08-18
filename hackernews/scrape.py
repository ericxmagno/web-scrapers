import requests
from bs4 import BeautifulSoup
import pprint

def create_custom_hn(links,subtext):
    hn = []
    
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href')
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    
    return sort_stories_by_votes(hn)

def sort_stories_by_votes(stories):
    return sorted(stories, key=lambda item: item['votes'], reverse=True)

links, subtext = [], []
for i in range(1,3):
    response = requests.get(f'https://news.ycombinator.com/news?p={i}')
    soup = BeautifulSoup(response.text, 'html.parser')
    links.extend(soup.select('.storylink'))
    subtext.extend(soup.select('.subtext'))
print(links)

pprint.pprint(create_custom_hn(links,subtext))
