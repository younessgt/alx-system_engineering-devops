#!/usr/bin/python3
""" script containing the recurse function """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """ recursive function that  returns a list containing the titles
    of all hot articles for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    headers = {"User-Agent": "RedditApiTest/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if data:
            children = data.get('data').get('children')
            for child in children:
                title = child.get('data').get('title')
                hot_list.append(title)
            after = data.get('data').get('after')
            if after is not None:
                recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
