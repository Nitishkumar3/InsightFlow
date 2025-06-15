import requests

def upload_image_to_wordpress(image_url, alt_text):
    wordpress_url = 'https://techmedok.com/wp-json/custom/v1/generate-image-id'
    payload = {
        'url': image_url,
        'alt': alt_text
    }
    response = requests.post(wordpress_url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def publish_wp_post(title, content, categories, thumbnail_url, thumbnail_alt, status):
    site_url = "https://techmedok.com"
    username = "nitishkumar"
    password = "e7ecyj7zy2!"

    auth_url = f"{site_url}/wp-json/api/v1/token"
    payload = {
        "username": username,
        "password": password,
    }
    response = requests.post(auth_url, json=payload)

    if response.status_code == 200:
        data = response.json()
        access_token = data["jwt_token"]
    else:
        return False

    image_id = upload_image_to_wordpress(thumbnail_url, thumbnail_alt)
    if not image_id:
        return False

    post_url = f"{site_url}/wp-json/wp/v2/posts"
    data = {
        "title": title,
        "content": content,
        "status": status,
        "author": 1,  # The author ID; usually set to 1 for admin user
        "categories": categories,
        "featured_media": image_id
    }
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(post_url, json=data, headers=headers)

    if response.status_code == 201:
        return True
    else:
        return False

# Define the parameters for the post
title = "New Post Title"
content = "<p>This is the content of the new post.</p>"
categories = [1]  # Category IDs as a list
thumbnail_url = "https://images.pexels.com/photos/3738355/pexels-photo-3738355.jpeg"
thumbnail_alt = "Sample Alt Text"
status = "draft"  # or "publish" for publishing immediately

# Publish the post
if publish_wp_post(title, content, categories, thumbnail_url, thumbnail_alt, status):
    print("Post published successfully.")
else:
    print("Failed to publish the post.")
