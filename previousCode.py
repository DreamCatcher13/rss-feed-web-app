import feedparser
from datetime import date, timedelta, datetime

URLS = [
    "https://azurecomcdn.azureedge.net/en-us/updates/feed/",
    "https://www.wired.com/feed/category/security/latest/rss",
    "https://feeds.arstechnica.com/arstechnica/technology-lab",
    #"https://www.nasa.gov/news-release/feed/",
]

## CREATE a custom class  or model


def getFeeds(urls=URLS):
    """function to create a list of feeds from different urls""" 

    latest = []
    for link in urls:
        feed = feedparser.parse(link)
        newEnt = []
        for e in feed.entries:
            if ((date.today()-timedelta(days=5)) <= datetime.strptime((str.join(" ", e.published.split()[:-1])), '%a, %d %b %Y %H:%M:%S').date() <= date.today()):
                newEnt.append(e)
        feed.entries = newEnt[:]
        latest.append(feed)   
    return latest


        # print("Feed Title:", feed.feed.title)
        # print("Feed Description:", feed.feed.description)
        # print("Feed Link:", feed.feed.link)
        #     print("Entry Title:", entry.title)
        #     print("Entry Link:", entry.link)
        #     print("Entry Published Date:", entry.published)
        #     print("Entry Summary:", entry.summary)
        #     print(type(entry.published))
        #     print("\n

#for entry in f.entries[:5]:
#            d = str.join(" ", entry.published.split()[:-1])
#            dt = datetime.strptime(d, '%a, %d %b %Y %H:%M:%S').date()
#            if (date.today()-timedelta(days=2)) <= dt <= date.today():
#                pass # last 2 days




#Wed, 22 Nov 2023 17:58:56 +0000
#datetime.strptime(st, '%a, %d %b %Y %H:%M:%S %z').date()
#https://medium.com/@jonathanmondaut/fetching-data-from-rss-feeds-in-python-a-comprehensive-guide-a3dc86a5b7bc


