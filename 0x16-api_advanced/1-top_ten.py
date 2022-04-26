#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """If not a valid subreddit, print None"""
    url = "https://www.reddit.com/r/{:s}/hot.json".format(subreddit)
    headers = {'User-agent': 'api_advanced'}
    params = {'limit': 10}
    res = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if res.status_code != 200:
        print(None)
        return
    res = res.json()
    top = res['data']['children']

    if len(top) == 0:
        print(None)
    else:
        for t in top:
            print(t['data'].get('title', None))
