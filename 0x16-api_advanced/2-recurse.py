#!/usr/bin/python3
""" Recursively fetch all hot posts for a given subreddit."""
import requests


def fetch_all_hot_posts(subreddit, hot_posts_list=[], after_token=None):
    """
    Recursively fetch all hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_posts_list (list): A list to store the titles of hot posts.
        after_token (str): The token for pagination to fetch the next set
        of posts.

    Returns:
        list: A list containing the titles of all hot posts.
    """
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'}
    params = {'limit': 100}
    if after_token:
        params['after'] = after_token

    try:
        response = requests.get(api_url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            response_data = response.json()
            posts = response_data['data']['children']
            for post in posts:
                hot_posts_list.append(post['data']['title'])
            after_token = response_data['data'].get('after')
            if after_token:
                return fetch_all_hot_posts(subreddit, hot_posts_list,
                                           after_token)
            else:
                return hot_posts_list
        else:
            return None
    except requests.RequestException as request_error:
        print(f"An error occurred: {request_error}")
        return None
    except ValueError as json_error:
        print(f"Error decoding JSON: {json_error}")
        return None
    except KeyError as key_error:
        print(f"Expected key not found in response: {key_error}")
        return None


# Alias to maintain compatibility with 2-main.py
recurse = fetch_all_hot_posts
