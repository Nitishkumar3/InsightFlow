from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost, EditPost
from wordpress_xmlrpc.methods.media import UploadFile
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.exceptions import ServerConnectionError

def PostWordPress(title, content, image_path):
    wp_url = 'https://ai.techmedok.com/xmlrpc.php'
    wp_username = 'nitishkumar'
    wp_password = '818S3KV0dUNdafFVnNbB'

    try:
        client = Client(wp_url, wp_username, wp_password)
    except ServerConnectionError:
        return False

    try:
        user_info = client.call(GetUserInfo())
    except Exception:
        return False

    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = 'publish'

    try:
        post_id = client.call(NewPost(post))
    except Exception:
        return False

    # Now let's upload the featured image
    image_name = image_path.split('/')[-1]

    data = {
        'name': image_name,
        'type': 'image/png',  # Change this based on the file type
    }

    with open(image_path, 'rb') as img:
        data['bits'] = img.read()

    try:
        response = client.call(UploadFile(data))
        attachment_id = response['id']
    except Exception:
        return False

    # Set the uploaded image as the featured image for the post
    post.thumbnail = attachment_id

    try:
        client.call(EditPost(post_id, post))
        return True
    except Exception:
        return False

# # Example usage:
# title = 'My New Post'
# content = """
# This is the content of my new post.
# """
# image_path = 'thumbnails/NTPC eyes $50 billion capex to transform into a complete energy company.jpg'
# success = create_wordpress_post(title, content, image_path)
# print(success)
