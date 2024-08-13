#!/usr/bin/python3
"""
    Print the titles of the top 10 hot posts for a given subreddit.
"""
import requests


def print_top_ten_hot_posts(subreddit):
    """
    Print the titles of the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    try:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
        headers = {'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()

            # Extract and print the titles of the first 10 hot posts
            hot_posts = json_data['data']['children']
            for post in hot_posts:
                print(post['data']['title'])
        else:
            # If the subreddit not found or any other error occurs, print None
            print(None)
    except requests.RequestException as request_error:
        # Handle network-related errors
        print(f"An error occurred: {request_error}")
        print(None)
    except ValueError as json_error:
        # Handle JSON decoding errors
        print(f"Error decoding JSON: {json_error}")
        print(None)
    except KeyError as key_error:
        # Handle cases where the expected data is not in the response
        print(f"Expected key not found in response: {key_error}")
        print(None)
