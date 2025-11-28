import re


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

    