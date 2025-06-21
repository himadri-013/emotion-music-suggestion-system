import streamlit as st
from deepface import DeepFace
from emotion_mapper import emotion_to_genre
from spotify_utils import get_recommendations
from PIL import Image

st.set_page_config(page_title="Mood2Music", layout="centered")
st.title("🎭 Mood2Music: Emotion-Based Song Recommender")
st.write("Take a selfie, let us detect your mood, and we'll recommend songs just for you!")

# Upload image using Streamlit camera
img = st.camera_input("📸 Take a selfie")

if img:
    with open("temp.jpg", "wb") as f:
        f.write(img.getvalue())

    try:
        # Detect emotion using DeepFace
        result = DeepFace.analyze("temp.jpg", actions=["emotion"])
        emotion = result[0]["dominant_emotion"]
        st.success(f"😄 Detected Emotion: **{emotion.capitalize()}**")

        # Get genre and song recommendations
        genre = emotion_to_genre(emotion)
        tracks = get_recommendations(genre)

        st.markdown(f"### 🎧 Songs for a {emotion.capitalize()} Mood")
        for track in tracks:
            st.image(track["img"], width=100)
            st.markdown(f"[**{track['name']}** - *{track['artist']}*]({track['url']})", unsafe_allow_html=True)
            st.markdown("---")

    except Exception as e:
        st.error("❌ Failed to analyze image. Please take a clearer selfie.")
        st.text(f"Error: {e}")

