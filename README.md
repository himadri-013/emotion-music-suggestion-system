# 🎧 Emotion-Based Music Recommendation System
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)


This is an AI-powered music recommendation app that detects your **facial emotion via webcam** and suggests songs that match your mood using the **Spotify API**.

Hosted on [Streamlit Cloud](https://streamlit.io/cloud), it uses **DeepFace** for emotion recognition and **Spotipy** for fetching music data.

---

## 💡 Features

- 🔍 Real-time emotion detection via webcam
- 🤖 DeepFace-based facial expression analysis
- 🎵 Spotify API integration for mood-specific song suggestions
- 🖥️ Fully interactive web interface using Streamlit
- ☁️ Deployable on Streamlit Cloud with GitHub + secrets management

---

## 📸 How It Works

1. You launch the app in your browser.
2. The webcam activates and captures your face.
3. Emotions like `Happy`, `Sad`, `Angry`, etc. are predicted.
4. Based on detected emotions, songs are pulled from a curated Spotify dataset.
5. 🎶 You get clickable music links — ready to enjoy!

---

## 🚀 Deployment

### 1. Clone this repository

```bash
git clone https://github.com/your-username/emotion-music-recommender.git
cd emotion-music-recommender
