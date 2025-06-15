import requests
from bs4 import BeautifulSoup
import os
import mimetypes

import re

def CleanFileName(name):
    invalid_chars = r'[\\/:\*\?"<>\|]'
    clean_name = re.sub(invalid_chars, '', name)
    return clean_name


def DownloadThumbnail(urls, title):
    if not os.path.exists("thumbnails"):
        os.makedirs("thumbnails")

    title = CleanFileName(title)

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

# links = ['https://www.livemint.com/companies/news/ntpc-eyes-50-billion-capex-to-transform-into-a-complete-energy-company-11717929812272.html', 'https://www.qcintel.com/biofuels/article/india-s-ntpc-eyes-50bn-capex-for-saf-methanol-hydrogen-output-25526.html', 'https://www.pressreader.com/india/hindustan-times-bathinda/20240610/282381224699050', 'https://www.linkedin.com/posts/ashok-kumar-57b491134_news-headlines-from-business-news-agencies-activity-7206105336951304194-RO4p', 'https://www.newsnow.com/us/%3Fsearch%3D%2522NTPC%2522%26lang%3Den%26searchheadlines%3D1']
# title = "NTPC eyes $50 billion capex to transform into a complete energy company"

# downloaded_image = DownloadThumbnail(links, title)

# print("Image downloaded:", downloaded_image)