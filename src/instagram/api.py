import requests
import random

def fetch_instagram_posts(api_url, access_token, count=3):
    response = requests.get(f"{api_url}/users/self/media/recent?access_token={access_token}")
    if response.status_code == 200:
        posts = response.json().get('data', [])
        return random.sample(posts, min(count, len(posts)))
    return []