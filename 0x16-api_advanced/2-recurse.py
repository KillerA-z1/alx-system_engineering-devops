#!/usr/bin/python3
"""
    Recursively fetch all hot posts for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'
    }

    # Parameters for pagination
    params = {'limit': 100}  # Maximum allowed by Reddit API
    if after:
        params['after'] = after

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract posts from the response
            posts = data['data']['children']

            # If no posts are returned, we've reached the end
            if not posts:
                return hot_list

            # Add titles of current page to hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Get 'after' for next page
            after = data['data']['after']

            # If there's another page, make a recursive call
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        elif response.status_code == 404:
            # Subreddit not found
            return None
        else:
            # Other error occurred
            return None
    except requests.RequestException:
        # Handle network-related errors
        return None
    except (ValueError, KeyError):
        # Handle JSON decoding errors or unexpected data structure
        return None
