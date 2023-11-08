#!/usr/bin/python3
"""2-recurse.py"""


import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""

    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'YourUniqueUserAgent/1.0'}

    # Construct the URL for the subreddit's hot posts with pagination
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Include the 'after' parameter for pagination
    if after:
        url += f'?after={after}'

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is not valid
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json()

    # Extract titles from the current page and add them to the hot_list
    hot_list.extend(post['data']['title'] for post in data.get('data', {}).get('children', []))

    # Check if there are more pages (next page) and continue recursively
    if data['data']['after']:
        return recurse(subreddit, hot_list, data['data']['after'])
    else:
        return hot_list

