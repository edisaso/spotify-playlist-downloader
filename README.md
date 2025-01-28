# 🎵 Spotify Playlist Downloader! 🎶

Welcome to the **Spotify Playlist Downloader**! This script fetches tracks from your Spotify playlist and downloads their audio from YouTube as MP3 files. Now you can jam to your favorite tunes offline! 🚀

---

## ⚡ Features

- ✅ **Spotify Authorization**: Securely connects to your Spotify account.
- ✅ **Playlist Fetching**: Grabs tracks from your favorite Spotify playlists.
- ✅ **YouTube MP3 Downloading**: Converts tracks into high-quality MP3s via YouTube.

---

## 🛠️ Setup & Requirements

### Prerequisites
1. **Python 3.8+**
2. Install required libraries:
   ```bash
   pip install requests yt-dlp
   ```
3. A Spotify Developer account. Sign up [here](https://developer.spotify.com/).

---

## 🚀 How to Use

### 1️⃣ Get Your Spotify API Credentials
- Go to your [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
- Create an app and copy the **Client ID** and **Client Secret**.
- Set the redirect URI in your app settings to: `http://localhost:8888/callback`.

### 2️⃣ Clone This Repo
```bash
git clone https://github.com/edisaso/spotify-playlist-downloader.git
cd spotify-playlist-downloader
```

### 3️⃣ Configure the Script
Replace the placeholders in the script with your Spotify credentials:

```python
CLIENT_ID = 'Replace with your Client ID'
CLIENT_SECRET = 'Replace with your Client Secret'
REDIRECT_URI = 'http://localhost:8888/callback'
playlist_id = '3lOVpptuk4I9eQtEcSDG5U'  # Replace with your playlist ID
```

### 4️⃣ Run the Script
```bash
python script.py
```
- Authorize the app when prompted. You'll be redirected to a URL—paste it back into the terminal when asked.
- Sit back and let the script work its magic! 🧙‍♂️

---

## 📂 Output
Downloaded MP3s will be saved in a `/downloads` folder in the same directory as the script.

---

## 📝 Notes

- Ensure the playlist you’re accessing is public or shared with your account.
- If downloading fails for a track, it will skip and move to the next one.

---

## 📢 Disclaimer
This script is for personal use only. Please respect copyright laws and use responsibly.

---

## 🤝 Contributing
Feel free to fork this repo, submit issues, or create pull requests. Let’s make this even better together!

---