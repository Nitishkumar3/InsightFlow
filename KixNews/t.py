from GeminiPro import GenAI
import requests
from bs4 import BeautifulSoup
import re
import json
import re
from datetime import datetime, timedelta

def Google(query):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    url_template = 'https://www.google.com/search?q={}'
    results = []
    query = query +" after:" + str((datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d'))
    url = url_template.format(query)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    urls = [link['href'] for link in links]
    for link in urls:
        results.append(link)

    links=[]
    for link in results:
        match = re.search(r'&url=(.*?)&ved=', link)
        if match:
            links.append(match.group(1))
    return links

def LinkSelection(Topic, Links):
    LinksString = "\n".join(Links)
    query = f"""
    You are a journalist assistant. From the given search results, select the URLs that seem most relevant and informative for writing an article on the topic: {Topic}.\n
    Search Results:\n{LinksString}\n\nPlease return the URLs that seem most relevant and informative for writing an article on the topic. 
    Respond with minimum 4 links and maximum any number of links in a Python-parseable list, separated by commas.
    Your response should be an Array of Links. Format: Each index should be enclosed within Double Quotes and All the Indexes should be collectively enclosed within Square Brackets.
    """
    SelectedLinks = GenAI(query)
    
    try:
        SelectedLinks = SelectedLinks.strip("```")
        SelectedLinks = json.loads(SelectedLinks)
    except Exception as e:
        print("")

    if isinstance(SelectedLinks, list):
        return SelectedLinks
    else:
       return LinkSelection(Topic, Links)
    
Topic = "Putin's North Korea Visit"
Links = Google(Topic)
print("Crawled Web for Sources")
print("-------")
print(Links)
print(len(Links))
print("-------")

SelectedLinks = LinkSelection(Topic, Links)
print("Sources are Selected")
print("-------")
print(SelectedLinks)
print(len(SelectedLinks))
print("-------")