#!/usr/bin/python3
""" script containing top_ten function """

import requests


def top_ten(subreddit):
    """ Displaying the titles of the first 10 hot posts listed
    for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "RedditTestApi/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if data:
            posts = data.get("data").get("children")
            for post in posts:
                title = post.get("data").get("title")
                print(title)
        else:
            return None
    else:
        return None
