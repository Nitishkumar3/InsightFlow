import requests
from bs4 import BeautifulSoup
import csv
import os

# RSS feed
url = "http://feeds.bbci.co.uk/news/rss.xml"
response = requests.get(url)

if response.status_code == 200:
#Parse the RSS feed
    soup = BeautifulSoup(response.content, 'xml')

#Extract information from <item> tags
    items = soup.find_all('item')
    news_items = []

    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        pub_date = item.find('pubDate').text

#Extract image URL if available
        media_content = item.find('media:content')
        if media_content and 'url' in media_content.attrs:
            image_url = media_content['url']
        else:
            image_url = None

        news_items.append({
            'title': title,
            'link': link,
            'pub_date': pub_date,
            'image_url': image_url
        })

#Write the data to a CSV file
# Specify the directory where you want to save the file

    save_directory = r'C:\\Users\\nitis\\Desktop\\BlogX\\AI Online Writer\\RSS\\'  # Update this path
    os.makedirs(save_directory, exist_ok=True)  # Create the directory if it doesn't exist
    csv_file = os.path.join(save_directory, 'bbc_news.csv')

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'link', 'pub_date', 'image_url'])
        writer.writeheader()
        writer.writerows(news_items)

    print(f"Data has been written to {csv_file} successfully.")

else:
    print(f"Failed to fetch the RSS feed. Status code: {response.status_code}")
