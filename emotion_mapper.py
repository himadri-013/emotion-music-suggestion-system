def emotion_to_genre(emotion):
    mapping = {
        "happy": "pop",
        "sad": "acoustic",
        "angry": "rock",
        "fear": "ambient",
        "neutral": "chill",
        "surprise": "dance",
        "disgust": "metal"
    }
    return mapping.get(emotion.lower(), "chill")

