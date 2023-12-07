import feedparser
from datetime import date, timedelta, datetime

URLS = [
    "https://azurecomcdn.azureedge.net/en-us/updates/feed/",
    "https://www.wired.com/feed/category/security/latest/rss",
    "https://feeds.arstechnica.com/arstechnica/technology-lab",
    "https://www.nasa.gov/news-release/feed/",
]

def getFeeds(urls=URLS):
    """function to create a list of feeds from different urls""" 

    feeds = []
    for link in urls:
        f = feedparser.parse(link)
        result = f"{f.feed.title}"
        # print("Feed Title:", feed.feed.title)
        # print("Feed Description:", feed.feed.description)
        # print("Feed Link:", feed.feed.link)
        for entry in f.entries[:5]:
            d = str.join(" ", entry.published.split()[:-1])
            dt = datetime.strptime(d, '%a, %d %b %Y %H:%M:%S').date()
            if (date.today()-timedelta(days=2)) <= dt <= date.today(): # last 2 days
                ent = f"\n\t* {entry.title}\n\t\t{entry.summary}\n\t\t{d}"
                result += ent
        feeds.append(result)
    return feeds
        #     print("Entry Title:", entry.title)
        #     print("Entry Link:", entry.link)
        #     print("Entry Published Date:", entry.published)
        #     print("Entry Summary:", entry.summary)
        #     print(type(entry.published))
        #     print("\n")


#Wed, 22 Nov 2023 17:58:56 +0000
#datetime.strptime(st, '%a, %d %b %Y %H:%M:%S %z').date()
#https://medium.com/@jonathanmondaut/fetching-data-from-rss-feeds-in-python-a-comprehensive-guide-a3dc86a5b7bc


