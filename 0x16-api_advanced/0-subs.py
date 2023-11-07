#!/usr/bin/python3
""" Script Containing  number_of_subscribers function """
import requests


def number_of_subscribers(subreddit):
    """ function that get the number of subscribers for a giver subreddit
    If an invalid subreddit is given, the function should return 0"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "RedditApiTest/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if data.get('data').get('dist') == 0:
            return 0
        else:
            subscribers = data.get('data').get('subscribers')
            return subscribers
    else:
        return 0
