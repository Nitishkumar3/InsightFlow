import feedparser

d = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')
for entry in d.entries:
    print(entry.title)
    print(entry.link)
    print(entry.published)
