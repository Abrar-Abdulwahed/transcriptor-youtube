from core.helpers import save_transcript_to_file, extract_video_id
from core.transcriptor_service import transcriptor;


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