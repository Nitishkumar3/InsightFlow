from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost, EditPost
from wordpress_xmlrpc.methods.media import UploadFile
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.exceptions import ServerConnectionError
from bs4 import BeautifulSoup
import string

def FormatHTML(html_string):
    soup = BeautifulSoup(html_string, "html.parser")
    for strong_tag in soup.find_all('strong'):
        strong_tag.unwrap()
    modified_html = str(soup)
    cleaned_string = ''.join(char for char in modified_html if char in string.printable)
    lines = cleaned_string.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith('<p>') and line.endswith('</p>'):
            cleaned_lines.append(line)
        elif line.startswith('<') and not line.startswith('<p>'):
            cleaned_lines.append(line)
        else:
            cleaned_lines.append(f"<p>{line}</p>")
    cleaned_string = '\n'.join(cleaned_lines)
    cleaned_string = cleaned_string.replace('<p><p>', '<p>').replace('</p></p>', '</p>')
    cleaned_string = cleaned_string.replace('<p></p>', '')
    return cleaned_string
    
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

    image_name = image_path.split('/')[-1]

    data = {
        'name': image_name,
        'type': 'image/png',  
    }

    with open(image_path, 'rb') as img:
        data['bits'] = img.read()

    try:
        response = client.call(UploadFile(data))
        attachment_id = response['id']
    except Exception:
        return False

    post.thumbnail = attachment_id

    try:
        client.call(EditPost(post_id, post))
        return True
    except Exception:
        return False