import requests

# Define the API endpoint and subreddit name
url = 'https://www.reddit.com/r/leagueoflegends/top/.json'
headers = {'User-agent': 'myBot/0.0.1'}

# Send the request to the API endpoint with the defined headers
response = requests.get(url, headers=headers)

# Parse the response data as JSON
data = response.json()

# Print the titles of the top 10 posts
for post in data['data']['children'][:10]:
    print(post['data']['title'])
