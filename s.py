import requests

# Define the URL of your WordPress site
wordpress_url = 'https://techmedok.com/wp-json/custom/v1/generate-image-id'

# Define the image URL and alt text
image_url = "https://cdn.deliciousbrains.com/content/uploads/2015/08/26231827/added-plaintext-field-json-response.png"
alt_text = 'Sample Alt Text'

# Define the payload (parameters)
payload = {
    'url': image_url,
    'alt': alt_text
}

# Send a POST request to the WordPress endpoint
response = requests.post(wordpress_url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Image ID received successfully
    image_id = response.json()
    print(f"Image ID: {image_id}")
else:
    # Request failed
    print(f"Failed to get image ID. Status code: {response.status_code}")
