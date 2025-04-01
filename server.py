from flask import Flask, jsonify, request
from flask_cors import CORS
from main import main 

app = Flask(__name__)
CORS(app)  

@app.route('/send_text', methods=['POST'])
def send_text():
    
    data = request.json
    received_link = data.get('text', 'Текст не получен')
    
    received_text = main(received_link)
    
    return jsonify({
        "status": "success",
        "message": f"{received_text}"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)