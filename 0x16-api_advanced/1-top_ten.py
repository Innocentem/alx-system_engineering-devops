import requests

def top_ten(subreddit):
    '''
    Print the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is not valid or does not exist, print None.
    '''
    user_agent = {'User-Agent': 'Innocentesalvatore'}
    url = f"https://www.reddit.com/r/{subreddit}/top/.json?limit=10"
    
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("No posts found for the subreddit:", subreddit)
    else:
        print("Invalid subreddit or request failed. Status code:", response.status_code)

if __name__ == "__main__":
    subreddit = input("Enter the subreddit: ")
    top_ten(subreddit)
