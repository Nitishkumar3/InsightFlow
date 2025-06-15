from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost, EditPost
from wordpress_xmlrpc.methods.media import UploadFile
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.exceptions import ServerConnectionError


wp_url = 'https://ai.techmedok.com/xmlrpc.php'
wp_username = 'nitishkumar'
wp_password = '818S3KV0dUNdafFVnNbB'

try:
    client = Client(wp_url, wp_username, wp_password)
except ServerConnectionError as e:
    raise

try:
    user_info = client.call(GetUserInfo())
except Exception as e:
    raise

post = WordPressPost()
post.title = 'My New Post'
post.content = """
This is the content of my new post.
"""
post.post_status = 'publish'

try:
    post_id = client.call(NewPost(post))
except Exception as e:
    raise

# Now let's upload the featured image
image_path = '1.webp'  # Replace with the path to your image
image_name = '1.webp'  # Replace with the image name

data = {
    'name': image_name,
    'type': 'image/png',  # Change this based on the file type
}

with open(image_path, 'rb') as img:
    data['bits'] = img.read()

try:
    response = client.call(UploadFile(data))
    attachment_id = response['id']
except Exception as e:
    raise

# Set the uploaded image as the featured image for the post
post.thumbnail = attachment_id

try:
    client.call(EditPost(post_id, post))
except Exception as e:
    raise
