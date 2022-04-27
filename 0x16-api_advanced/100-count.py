#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript
should count as javascript, but java should not)
"""

import requests


def hot_print(res, word_list, param, hot_dict):
    """
    count the repeated words
    """
    top = res.json()["data"].get("children")
    for hot in top:
        for hot_word in word_list:
            title = hot.get("data").get("title")
            if title is not None:
                words = title.split()
                for word in words:
                    if hot_word.lower() == word.lower():
                        hot_dict[hot_word] += 1

    if param is None:
        count = sorted(hot_dict.items(), key=lambda x: x[1], reverse=True)

        for k, v in count:
            if v != 0:
                print(f'{k}: {v}')


def count_words(subreddit, word_list, param1=None, hot_dict={}):
    """
    If no posts match or the subreddit is invalid, print nothing.
    """
    url = "https://www.reddit.com"
    res = requests.get("{}/r/{}/hot.json".format(url, subreddit),
                       headers={'User-Agent': 'api_advanced'},
                       params={'after': param1})

    if res.status_code != 200:
        return None

    if len(hot_dict) == 0:
        for elem in word_list:
            hot_dict[elem] = 0

    if res:
        after_n = res.json()["data"].get("after")
        if after_n:
            count_words(subreddit, word_list,
                        param1=after_n,
                        hot_dict=hot_dict)

            hot_print(res, word_list, param1, hot_dict)
            return hot_dict

        else:
            hot_print(res, word_list, param1, hot_dict)
            return hot_dict
    else:
        return None
