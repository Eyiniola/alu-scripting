#!/usr/bin/python3
"""0-subs.py"""

import requests

"""Reddit subscribers"""

def number_of_subscribers(subreddit):
  """Reddit subscribers"""     
    headers = {'User-Agent': 'YourUniqueUserAgent/1.0'}

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0

