import requests
import os
from dotenv import load_dotenv
load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")
RAPIDAPI_URL = os.getenv("RAPIDAPI_URL")

def transcriptor(video_id, lang):
    if not RAPIDAPI_KEY or not RAPIDAPI_HOST or not RAPIDAPI_URL:
        raise RuntimeError("Missing API configuration in .env file.")
     
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
    }

    querystring = {
        "video_id": video_id,
        "lang": lang,
    }

    response = requests.get(RAPIDAPI_URL, headers=headers, params=querystring)

    if response.status_code != 200:
        raise RuntimeError(f"API Error, {response.text}")

    data = response.json()
    video_info = data[0]
    transcription_text = video_info.get("transcriptionAsText", "")
    return transcription_text