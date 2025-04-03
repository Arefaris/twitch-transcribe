Small tool to feed Twitch or YouTube clips to the ChatGPT Whisper API and transcribe them. I built this tool mainly for language learning. Sometimes I just want to know the specific word while watching twitch stream but can't type it out by myself, or Im typing it wrong.
This repo includes chrome extension and flask server. 
You will need to install chrome extention using chrome dev tools to run this. 
Create .env file in root directory with your chatgpt api key. 
Be aware that this extension using gpt-4o-mini-transcribe api. Do your own research about cost.
Env file should look like this "API_KEY=YOURKEY"
You would have to install all the dependencies. Such as audio_extract, yt_dlp, and openai.
After that, run python server.py.
I did use AI to build this.
