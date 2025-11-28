import re
from transcriptor_service import transcriptor;


# Extract VIDEO ID
def extract_video_id(url):
    regex = r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid youtube URL") 

# save script text to file
def save_transcript_to_file(transcript_text, filename = "transcript.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(transcript_text)


if __name__ == "__main__":
    youtube_url = input("Enter the youtube URL: ").strip()
    lang_code = input("Enter the lang of content (ar/en): ").strip()

    try:
        video_id = extract_video_id(youtube_url)
        print("Transcripting... please wait.")
        transcript_text = transcriptor(video_id=video_id, lang=lang_code)
        save_transcript_to_file(transcript_text)
        print("Well Done!")
    except Exception as e:
        print(f"{e}")

    