import requests

def set_featured_image_from_url(url, alt_text, endpoint_url, username, password):
    """
    Sends a POST request to the WordPress endpoint to set the featured image.

    Args:
        url (str): The URL of the image.
        alt_text (str): The alt text for the image.
        endpoint_url (str): The URL of the WordPress endpoint.
        username (str): WordPress username with edit permissions.
        password (str): WordPress password.

    Returns:
        int: The image ID if successful, None otherwise.
    """

    data = {'image_url': url, 'alt_text': alt_text}
    auth = requests.auth.HTTPBasicAuth(username, password)

    try:
        response = requests.post(endpoint_url, json=data, auth=auth)
        response.raise_for_status()  # Raise an exception for error status codes

        if response.status_code == 200:
            response_json = response.json()
            return response_json.get('image_id')
        else:
            print("Error:", response.text)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    return None

# Example usage:
image_url = "https://www.cloudways.com/blog/wp-content/uploads/image01-85.png"
alt_text = "My Image Description"
endpoint_url = "https://techmedok.com/wp-json/fifu/v1/set_featured_image"
username = "nitishkumar"
password = "e7ecyj7zy2!"

image_id = set_featured_image_from_url(image_url, alt_text, endpoint_url, username, password)

if image_id:
    print("Image ID:", image_id)
else:
    print("Failed to set featured image.")