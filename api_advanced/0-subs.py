#!/usr/bin/python3
"""0-subs.py"""
import requests

def number_of_subscribers(subreddit):
    """ Set a custom User-Agent to avoid "Too Many Requests" errors """
    headers = {'User-Agent': 'YourUniqueUserAgent/1.0'}

    """ Construct the URL for the subreddit """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    """ Send a GET request to the Reddit API """
    response = requests.get(url, headers=headers, allow_redirects=False)

    """ Check if the request was successful (status code 200) """
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0

