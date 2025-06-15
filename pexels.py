import requests

url = "https://api.pexels.com/v1/search"
query_params = {
    "query": "Tech",
    "per_page": 1,
    "orientation": "landscape"
}
headers = {
    "Authorization": "it6DqZSG3KKkBbbRndR8PWcUroVHCnes8vBMjLHeR0KVnZAWfQiOrv68"
}

response = requests.get(url, params=query_params, headers=headers)
src = response.json()["photos"][0]["src"]["original"]
print(src)
