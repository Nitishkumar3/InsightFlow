from WebCrawler import Google, LinkSelection, ArticleScraper, CleanText
from Writer import Writer
from ThumbnailDownload import DownloadThumbnail
from WordPressPublish import PostWordPress, FormatHTML
from time import time
from markdown import markdown

s = time()

Topic = "NTPC eyes $50 billion capex to transform into a complete energy company"

Links = Google(Topic)
print("Crawled Web for Sources")
print("-------")

SelectedLinks = LinkSelection(Topic, Links)
print("Sources are Selected")
print("-------")

Context = ""
for i in range(len(SelectedLinks)):
    Source = ArticleScraper(SelectedLinks[i])
    Source = CleanText(Source)
    Context = Context + f"Source {i+1}: " + Source + "\n"

print("Context Compiled")
print("-------")

Title, HTML = Writer(Topic, Context)

if Title.startswith(("'", '"')) and Title.endswith(("'", '"')):
    Title = Title[1:-1]

print("Article Generated")
print("-------")

ThumbnailImage = DownloadThumbnail(SelectedLinks, Title)

print("Thumbnail Downloaded")
print("-------")

HTML = FormatHTML(HTML)
Post = PostWordPress(Title, HTML, ThumbnailImage)

with open(f"./out/md.html", 'w', encoding='utf-8') as file:
    file.write(markdown(HTML))

with open("./out/html.txt", "w") as file:
    file.write(HTML)

if Post:
    print("Published")
    e = time()
    print(f"{e-s} seconds")