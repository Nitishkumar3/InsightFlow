from WebCrawler import Google, LinkSelection, ArticleScraper, CleanText
from Writer import Writer
from time import time
from markdown import markdown
from GeminiPro import GenAI
from ThumbnailDownload import DownloadThumbnail
from WordPressPublish import PostWordPress

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

print("Article Generated")
print("-------")

# with open(f"./out/Article/Article.html", 'w', encoding='utf-8') as file:
#     file.write(markdown(HTML))

e = time()

print(f"Article Generated in {e-s} seconds.")


ThumbnailImage = DownloadThumbnail(SelectedLinks, Title)

Post = PostWordPress(Title, HTML, ThumbnailImage)

print(Post)
