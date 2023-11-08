#!/usr/bin/python3
"""number_of_subscribers

This module defines a function to retrieve the number of subscribers for a Reddit subreddit using the Reddit API.

"""

import requests

def number_of_subscribers(subreddit):
    """Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit for which you want to retrieve the number of subscribers.

    Returns:
        int: The number of subscribers for the subreddit. If the subreddit is not found or there's an issue with the request, it returns 0.

    """
    
    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'YourUniqueUserAgent/1.0'}

    # Construct the URL for the subreddit's about.json API endpoint
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send an HTTP GET request to the Reddit API with the custom User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # If the request is successful, parse the JSON response and extract the number of subscribers
        return response.json().get("data").get("subscribers")
    else:
        # If the subreddit is not found or there's an issue with the request, return 0
        return 0

