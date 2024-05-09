import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 404:
            return None

        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for post in results.get("children"):
            hot_list.append(post.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        else:
            return hot_list
    except Exception as e:
        print("Error:", e)
        return None

