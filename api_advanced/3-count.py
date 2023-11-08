#!/usr/bin/python3

"""3-count.py"""

import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Query Reddit API, count keywords, and print results.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list of str): List of keywords to count.
        counts (dict, optional): Dictionary to store keyword counts.
        after (str, optional): The 'after' parameter for pagination.

    Returns:
        None

    Recursively queries the Reddit API for hot articles in the specified subreddit,
    counts the occurrences of keywords from the word_list in the article titles,
    and prints the results sorted in descending order by count and ascending order
    alphabetically (if counts are the same). Words not found are skipped.

    """


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

    # Extract titles from the current page and count keyword occurrences
    for post in data.get('data', {}).get('children', []):
        title = post['data']['title'].lower()
        for word in word_list:
            if word in title and not title.startswith(word + '.') and not title.startswith(
                    word + '!') and not title.startswith(word + '_'):
                counts[word] = counts.get(word, 0) + 1

    # Check if there are more pages (next page) and continue recursively
    if data['data']['after']:
        return count_words(subreddit, word_list, counts, data['data']['after'])
    else:
        # Print results in descending order by count and ascending order alphabetically
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")


