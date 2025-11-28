import requests
from .config import load_api_config

api = load_api_config()
def transcriptor(video_id, lang):
    headers = {
        "x-rapidapi-key": api['key'],
        "x-rapidapi-host": api['host'],
    }

    querystring = {
        "video_id": video_id,
        "lang": lang,
    }

    response = requests.get(api['url'], headers=headers, params=querystring)

    if response.status_code != 200:
        raise RuntimeError(f"API Error, {response.text}")

    data = response.json()
    video_info = data[0]
    transcription_text = video_info.get("transcriptionAsText", "")
    return transcription_text