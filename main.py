from audio_extract import extract_audio
import yt_dlp
import openai
import os
from pathlib import Path
from dotenv import load_dotenv
speech_file_path = Path(__file__).parent / "speech.mp3"

load_dotenv()

try:
    API_KEY = os.getenv("API_KEY")
    openai.api_key = API_KEY 
except Exception as e:
    print("There was an error with the openAI api. Did you include your api key in .env?: ",  e)

def download_clip(clip_url, output_path="clip.%(ext)s"):
    ydl_opts = {
        'outtmpl': output_path, 
        'format': 'worst',  
        'overwrites': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([clip_url])
    

def main(clip_url):
    try:
        download_clip(clip_url)
    except Exception as e:
        print("There was an error while downloading: ", e)

    try:
        extract_audio(input_path="./clip.mp4", output_path="./clip.mp3", overwrite=True)
    except Exception as e:
        print("There was an error while extracting audio: ", e)

    try:
        text = transcribe()
    except Exception as e:
        print("There was an error while transcribing audio: ", e)
    return text
   
def transcribe():
    audio_file= open("clip.mp3", "rb")
    transcription = openai.audio.transcriptions.create(
    model="gpt-4o-mini-transcribe", 
    file=audio_file
)
    print(transcription.text)
    return transcription.text

def text_to_speech(text): 
    with openai.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input=text,
    instructions="Speak in a cheerful and positive tone.",
) as response:
        response.stream_to_file(speech_file_path)
        
if __name__ == "__main__":
    main()
