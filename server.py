from flask import Flask, jsonify, request
from flask_cors import CORS
from main import main 

app = Flask(__name__)
CORS(app)  # Это позволит избежать проблем с CORS при запросах из расширения

@app.route('/get_text', methods=['GET'])
def get_text():
    # Здесь может быть любой текст, который вы хотите отправить
    return jsonify({"text": "Это текст с сервера Python!"})


@app.route('/send_text', methods=['POST'])
def send_text():
    # Получаем данные из запроса
    data = request.json
    received_link = data.get('text', 'Текст не получен')
    
    received_text = main(received_link)
    
    # Отправляем ответ
    return jsonify({
        "status": "success",
        "message": f"{received_text}"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)