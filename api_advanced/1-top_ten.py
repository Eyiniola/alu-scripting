#!/usr/bin/python3 
"""top_ten_posts

This module defines a function to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.

"""

import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit for which you want to retrieve the hot posts.

    Returns:
        None

    Prints the titles of the first 10 hot posts for the specified subreddit. If the subreddit is not found or there's an issue with the request, it prints 'None'.

    """
     headers = {'User-Agent': 'YourUniqueUserAgent/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title', 'Title not available'))
    else:
        print(None)
