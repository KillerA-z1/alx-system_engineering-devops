#!/usr/bin/python3
"""
    Count occurrences of words in the titles of hot posts in a given subreddit.
"""
from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Count occurrences of words in the titles of hot posts in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to count in the titles.
        after_token (str, optional): The token for pagination to fetch the next
        set of posts.
        word_counter (Counter, optional): A Counter object to store word counts

    Returns:
        Counter: A Counter object containing the word counts.
    """
    if word_count is None:
        word_count = Counter()

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
                print_results(word_count, word_list)
                return

            # Process titles of current page
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    word = word.lower()
                    word_count[word] += sum(
                        1 for w in title.split() if w == word)

            # Get 'after' for next page
            after = data['data']['after']

            # If there's another page, make a recursive call
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                print_results(word_count, word_list)
        elif response.status_code == 404:
            # Subreddit not found
            return
        else:
            # Other error occurred
            return
    except requests.RequestException:
        # Handle network-related errors
        return
    except (ValueError, KeyError):
        # Handle JSON decoding errors or unexpected data structure
        return


def print_results(word_count, word_list):
    # Create a list of tuples (word, count) for words that appear in the titles
    results = [(word.lower(), count) for word,
               count in word_count.items() if count > 0]

    # Sort results by count (descending) and then alphabetically
    results.sort(key=lambda x: (-x[1], x[0]))

    # Print results
    for word, count in results:
        print(f"{word}: {count}")
