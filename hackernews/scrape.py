import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

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

pprint.pprint(create_custom_hn(links,subtext))
