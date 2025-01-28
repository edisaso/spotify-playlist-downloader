import requests
import webbrowser
import yt_dlp

# Replace with your Spotify API credentials
CLIENT_ID = 'Replace with your Client ID'
CLIENT_SECRET = 'Replace with your Client Secret'
REDIRECT_URI = 'http://localhost:8888/callback'  # Must match your Spotify app settings

# Step 1: Redirect user to Spotify's authorization page
auth_url = 'https://accounts.spotify.com/authorize'
auth_params = {
    'client_id': CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': REDIRECT_URI,
    'scope': 'playlist-read-private',  # Required scope for accessing private playlists
}
webbrowser.open(f"{auth_url}?{'&'.join([f'{k}={v}' for k, v in auth_params.items()])}")

# Step 2: Get the authorization code from the redirect URL
print("After authorizing, you'll be redirected to a URL. Paste the full URL here:")
redirect_url = input("Paste the URL: ")
auth_code = redirect_url.split('code=')[1].split('&')[0]

# Step 3: Exchange the authorization code for an access token
token_url = 'https://accounts.spotify.com/api/token'
token_response = requests.post(token_url, data={
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': REDIRECT_URI,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
token_data = token_response.json()
access_token = token_data['access_token']

# Step 4: Fetch playlist data
playlist_id = '3lOVpptuk4I9eQtEcSDG5U'  # <---------------------------------------------------------------Replace with your playlist ID
headers = {
    'Authorization': f'Bearer {access_token}'
}
playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
playlist_response = requests.get(playlist_url, headers=headers)
playlist_data = playlist_response.json()

# Function to download audio from YouTube
def download_audio(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'downloads/%(title)s.%(ext)s',  # Save in a "downloads" folder
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([f"ytsearch:{query}"])
            print(f"Downloaded: {query}")
        except Exception as e:
            print(f"Failed to download {query}: {e}")

# Step 5: Print track information and download audio
if 'tracks' in playlist_data:
    for track in playlist_data['tracks']['items']:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        query = f"{track_name} {artist_name}"
        print(f"Searching for: {query}")
        download_audio(query)
else:
    print("Error: 'tracks' key not found in the API response.")
    print(playlist_data)  # Print the full response for debugging