
from SelectRSS import CollectRSS, SelectTitles, rss_urls
from BetaWrite import WritePublish

CSV = CollectRSS(rss_urls)
print("1")
Titles = SelectTitles(CSV)
print("2")

SelectedTitles = Titles[2:8]

print("Titles Selected:")
print(SelectedTitles)
print(len(SelectedTitles))
print("-------")

for Topic in SelectedTitles:
    WritePublish(Topic)