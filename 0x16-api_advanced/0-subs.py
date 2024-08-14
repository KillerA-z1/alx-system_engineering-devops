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
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'
    }

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response is a redirect
        if response.status_code in (301, 302):
            return 0
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is not found or any other error occurs, return 0
            return 0
    except requests.RequestException as e:
        # Handle network-related errors
        print(f"An error occurred: {e}")
        return 0
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error decoding JSON: {e}")
        return 0
    except KeyError as e:
        # Handle cases where the expected data is not in the response
        print(f"Expected key not found in response: {e}")
        return 0
