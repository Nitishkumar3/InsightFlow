import requests
from bs4 import BeautifulSoup
import os
import mimetypes
import re

def DownloadThumbnail(urls, title):
    if not os.path.exists("thumbnails"):
        os.makedirs("thumbnails")
    title = re.sub(r'[\\/:\*\?"<>\|]', '', title)
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            og_tags = soup.find_all('meta', attrs={'property': 'og:image'})
            if og_tags:
                thumbnail_url = og_tags[0]['content']
                image_response = requests.get(thumbnail_url)
                image_response.raise_for_status() 
                content_type = image_response.headers.get('content-type')
                extension = mimetypes.guess_extension(content_type)
                
                image_filename = os.path.join("thumbnails", f"{title}{extension}")
                with open(image_filename, 'wb') as image_file:
                    image_file.write(image_response.content)
                return image_filename
        except Exception as e:
            print(f"Error scraping and downloading thumbnail for {url}: {e}")
    return None