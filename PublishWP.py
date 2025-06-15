import requests

Title = "New Post Title"
Content = "<p>This is the content of the new post.</p>"
Categories = [1]  # Category IDs as a list
ThumbnailURL = "https://images.pexels.com/photos/3738355/pexels-photo-3738355.jpeg"
ThumbnailAlt = "s"
Status = "draft"

def PublishWP(Title, Content, Categories, ThumbnailURL, ThumbnailAlt, Status):
    SiteURL = "https://techmedok.com"
    Username = "nitishkumar"
    Password = "e7ecyj7zy2!"

    auth_url = f"{SiteURL}/wp-json/api/v1/token"
    payload = {
        "username": Username,
        "password": Password,
    }
    response = requests.post(auth_url, json=payload)

    if response.status_code == 200:
        data = response.json()
        access_token = data["jwt_token"]
    else:
        return False

    post_url = f"{SiteURL}/wp-json/wp/v2/posts"
    data = {
        "title": Title,
        "content": Content,
        "status": Status,
        "author": 1,  # The author ID; usually set to 1 for admin user
        "categories": Categories,
        "featured_media": 6123

    }
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(post_url, json=data, headers=headers)

    if response.status_code == 201:
        return True
    else:
        return False

print(PublishWP(Title, Content, Categories, ThumbnailURL, ThumbnailAlt, Status))