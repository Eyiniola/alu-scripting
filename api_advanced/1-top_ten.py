#!/usr/bin/python3
"""getting the top ten hottest post"""



import requests

def top_ten(subreddit):

    headers = {'User-Agent': 'YourUniqueUserAgent/1.0'}


    url = f'https://www.reddit.com/r/{subreddit}/about.json'


    response = requests.get(url, headers=headers, allow_redirects=False)


    if response.status_code == 200:
        return response.json().get("data").get("top ten")
    else:
        return None
