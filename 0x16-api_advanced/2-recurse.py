#!/usr/bin/python3
""" Python Script """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Python Method """
    link = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'mechken.atef@gmail.com'
    }

    reddit_req = requests.get(link, headers=headers)
    reddit_info = reddit_req.json().get("data")
    if reddit_info is None:
        return None
    hot_list += reddit_info.get("children", [])
    after = reddit_info.get("after", None)
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list
