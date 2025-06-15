import feedparser
import pandas as pd
from dateutil import parser
from datetime import datetime, timedelta, timezone
from io import StringIO
from GeminiPro import GenAI
import re
import json

rss_urls = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "http://rss.cnn.com/rss/edition_world.rss",
    "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
    "https://www.yahoo.com/news/rss/world/",
    "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms"
]

def ExtractData(text):
    try:
        pattern = re.compile(r'\[\s*"[^"]*"(?:\s*,\s*"[^"]*")*\s*\]', re.DOTALL)
        match = pattern.search(text)
        if match:
            data = json.loads(match.group())
            return data
        else:
            return []
    except Exception as e:
        return []



def CollectRSS(rss_urls):
    data = []
    two_days_ago = datetime.now(timezone.utc) - timedelta(days=1)

    for rss_url in rss_urls:
        feed = feedparser.parse(rss_url)
        feed_title = feed.feed.get('title', 'No feed title')
        for entry in feed.entries:
            title = entry.get('title', 'No title')
            link = entry.get('link', 'No link')
            published = entry.get('published', 'No published date')
            if published != 'No published date':
                published_date = parser.parse(published)
                if published_date >= two_days_ago:
                    published = published_date.isoformat()
                    data.append({
                        'Publication': feed_title,
                        'Title': title,
                        'Link': link,
                        'Date Published': published
                    })

    df = pd.DataFrame(data)

    # print(df)

    df.to_csv("news.csv", index=False)

    csv_string = StringIO()
    df.to_csv(csv_string, index=False)
    csv_string.seek(0)  
    csv_string = csv_string.getvalue()
    return csv_string

def SelectTitles(CSV):
    query= f"""
    from the below csv select news titles which are important and combine similar news in different publication into one title and list out the titles in the format of python list.
    Note: Select only the most important titles and make sure that output length is minimal. Also combine similar titles into one and make it more informative.
    CSV:
    {CSV}
    """

    Titles = GenAI(query, "gemini-1.5-pro", 8192)

    try:
        Titles = ExtractData(Titles)
    except Exception as e:
        print(e)

    if isinstance(Titles, list) and Titles:
        return Titles
    else:
       return SelectTitles(CSV)


def FineSelectTitles(Titles):
    query= f"""
    combine all the similar titles into one. Output should be in the format of python array.

    {Titles}
    """

    SelectedTitles = GenAI(query, "gemini-1.5-pro", 8192)

    try:
        SelectedTitles = ExtractData(SelectedTitles)
    except Exception as e:
        print(e)

    if isinstance(SelectedTitles, list) and SelectedTitles:
        return SelectedTitles
    else:
       return FineSelectTitles(Titles)