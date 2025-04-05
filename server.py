from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from main import main 
from main import text_to_speech

app = Flask(__name__)
CORS(app)  


@app.route('/play_audio', methods=['POST'])
def play_audio():
    data = request.json
    received_text = data.get('text', 'No value')
    text_to_speech(received_text)
    return send_file('speech.mp3', mimetype='audio/mpeg')

@app.route('/send_text', methods=['POST'])
def send_text():
    
    data = request.json
    received_link = data.get('text', 'No value')
    
    received_text = main(received_link)
    
    return jsonify({
        "status": "success",
        "message": f"{received_text}"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)