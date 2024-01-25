import feedparser
from datetime import date, timedelta, datetime

URLS = [
    "https://azurecomcdn.azureedge.net/en-us/updates/feed/",
    "https://www.wired.com/feed/category/security/latest/rss",
    "https://feeds.arstechnica.com/arstechnica/technology-lab",
    #"https://www.nasa.gov/news-release/feed/",
]

class Post():
    def __init__(self, source, title, description, dt, link):
        self. source = source
        self.title = title
        self.description = description
        self.dt = dt
        self.link = link


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
print(len(ent))