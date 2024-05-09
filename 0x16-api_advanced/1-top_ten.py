import requests
from sys import argv

def top_ten(subreddit):
    '''
    Prints the titles of the top ten posts for a given subreddit.
    '''
    user_agent = {'User-Agent': 'Lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=user_agent)
    try:
        data = response.json()
        for post in data.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script_name.py subreddit_name")
    else:
        subreddit = argv[1]
        top_ten(subreddit)

