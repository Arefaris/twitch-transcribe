document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("textInput");
    const button = document.getElementById("transcribeBtn");
    const output = document.getElementById("output");

    button.addEventListener("click", () => {
        const textToSend = input.value.trim();
        
        if (!textToSend){
            output.textContent = "Link not found"
        }

        output.textContent = "Transcribing..."

        fetch('http://localhost:5000/send_text', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: textToSend })
          })
          .then(response => {
            if (!response.ok) {
              throw new Error('Ошибка сети: ' + response.status);
            }
            return response.json();
          })
          .then(data => {
            output.textContent = data.message;
            // Очистить поле ввода после успешной отправки
            if (data.status === 'success') {
                input.value = '';
            }
          })
          .catch(error => {
            sendResultDiv.textContent = 'Ошибка: ' + error.message;
            console.error('Произошла ошибка при отправке:', error);
          });

    });
});
