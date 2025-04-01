from audio_extract import extract_audio
import yt_dlp
import openai
import os
from dotenv import load_dotenv

load_dotenv()  
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY 

def download_twitch_clip(clip_url, output_path="clip.%(ext)s"):
    ydl_opts = {
        'outtmpl': output_path,  # Формат имени файла
        'format': 'worst',  # Скачивает лучшее качество
        'overwrites': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([clip_url])

def main(clip_url):
    download_twitch_clip(clip_url)
    extract_audio(input_path="./clip.mp4", output_path="./clip.mp3", overwrite=True)
    text = transcribe()
    return text
   
def transcribe():
    audio_file= open("clip.mp3", "rb")
    transcription = openai.audio.transcriptions.create(
    model="gpt-4o-mini-transcribe", 
    file=audio_file
)
    print(transcription.text)
    return transcription.text
    
if __name__ == "__main__":
    main()
