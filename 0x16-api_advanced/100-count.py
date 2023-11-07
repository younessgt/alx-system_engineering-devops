#!/usr/bin/python3
""" count keywords """

import requests
from collections import Counter


def count_words(subreddit, word_list, after="", counter=None):
    """ recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords """

    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    headers = {"User-Agent": "RedditApiTest/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if counter is None:
        counter = Counter()

    if response.status_code == 200:
        try:
            data = response.json()
        except ValueError:
            return

        children = data.get('data').get('children')
        for child in children:
            title = child.get('data').get('title').lower()
            words = title.split()
            for word in words:
                if word in word_list:
                    # if i use a normal dictionary for counter
                    # instead of collections.Counter
                    # this will raise a KeyError because in Normal Dictionary
                    # when you attempt to increment a value for a
                    # key that doesn't exist, Python will raise a KeyError.
                    # Unlike collections.Counter
                    # if i want to use dictionary i should implement something
                    # like counter[word] = counter.get(word, 0) + 1
                    # to specify a default value when the key is not present
                    counter[word] += 1
        after = data.get('data').get('after')
        if after is not None:
            count_words(subreddit, word_list, after, counter)
        else:
            for word, count in sorted(counter.most_common()):
                print("{}: {}".format(word, count))
    else:
        return
