#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    If not a valid subreddit, return 0
    """

    url = "https://www.reddit.com/r/{:s}/about.json".format(subreddit)
    headers = {'User-agent': 'api_advanced'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 302:
        return 0
    if res.status_code == 404:
        return 0
    return res.json()['data'].get('subscribers', 0)
