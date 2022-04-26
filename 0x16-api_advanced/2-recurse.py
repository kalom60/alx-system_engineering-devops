#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """If not a valid subreddit, return None"""
    url = "https://www.reddit.com/r/{:s}/hot.json".format(subreddit)
    headers = {'User-agent': 'api_advanced'}
    params = {'after': after}
    res = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if res.status_code != 200:
        return None
    res = res.json()
    after = res['data']['after']
    top_list = res['data']['children']
    for top in top_list:
        hot_list.append(top['data']['title'])

    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    return recurse(subreddit, hot_list, after)
