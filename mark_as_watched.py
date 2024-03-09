import requests

# Trakt API settings
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'  # Access token obtained via OAuth
api_url = 'https://api.trakt.tv'
list_name = 'YOUR_LIST_NAME'  # Name of the list you want to operate on
username = 'YOUR_USERNAME'  # Your Trakt username

headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': client_id,
    'Authorization': f'Bearer {access_token}'
}

# Fetch the list
response = requests.get(f"{api_url}/users/{username}/lists/{list_name}/items", headers=headers)
list_items = response.json()

# Prepare the list of movies to be marked as watched
watched_movies = {
    "movies": [{"ids": {"trakt": movie['movie']['ids']['trakt']}} for movie in list_items if movie['type'] == 'movie']
}

# Mark the movies as watched
response = requests.post(f"{api_url}/sync/history", json=watched_movies, headers=headers)

if response.status_code == 201:
    print("Movies successfully marked as watched.")
else:
    print("An error occurred:", response.status_code, response.text)
