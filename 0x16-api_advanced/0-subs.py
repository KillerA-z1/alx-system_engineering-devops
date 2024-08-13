#!/usr/bin/python3
"""Reddit API interaction module"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid or
        an error occurs.
    """
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'User-agent': 'MyCustomUserAgent/1.0.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data['data']['subscribers']
    except (requests.RequestException, KeyError):
        return 0
