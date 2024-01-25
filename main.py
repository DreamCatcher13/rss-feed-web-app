import feedparser
from datetime import date, timedelta, datetime
import json

URLS = [
    "https://azurecomcdn.azureedge.net/en-us/updates/feed/",
    "https://www.wired.com/feed/category/security/latest/rss",
    "https://feeds.arstechnica.com/arstechnica/technology-lab",
    #"https://www.nasa.gov/news-release/feed/",
]

class Post():
    def __init__(self, source, title, description, dt, link):
        self.source = source
        self.title = title
        self.description = description
        self.dt = dt
        self.link = link

    def __str__(self):
        return f"{self.source}\n{self.dt} --  {self.title}"
    
    def toDict(self):
        obj = {
            'title': self.title,
            'desc': self.description,
            'date': self.dt,
            'link': self.link
        }
        return obj



def getFeeds(urls=URLS):
    """function to create a list of posts from different urls""" 

    latest = []
    for link in urls:
        feed = feedparser.parse(link)
        for e in feed.entries:
            if ((date.today()-timedelta(days=3)) <= datetime.strptime((str.join(" ", e.published.split()[:-1])), '%a, %d %b %Y %H:%M:%S').date() <= date.today()):
                p = Post(
                    feed.feed.title, 
                    e.title, 
                    e.summary, 
                    str.join(" ", e.published.split()[:-1]), 
                    e.link
                )
                latest.append(p)
    return latest

ent = getFeeds()

general = {}
for e in ent:
    if e.source in general.keys():
        general[e.source].append(e.toDict())
    else:
        general[e.source] = [e.toDict()]

with open("news.json", 'w') as f:
    json.dump(general, f, indent=4)

body = json.dumps(general)
print(body)
