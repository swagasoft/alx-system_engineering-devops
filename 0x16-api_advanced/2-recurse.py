#!/usr/bin/python3
"top recursive"

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        after = data['data']['after']
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
