import io
from gtts import gTTS

def save_audio(text: str) -> io.BytesIO:
    """
    Generate speech for `text` and return an in-memory MP3 file.
    """
    mp3_fp = io.BytesIO()
    tts = gTTS(text, lang='en')
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp