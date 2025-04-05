document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("textInput");
    const button = document.getElementById("transcribeBtn");
    const lisenBtn = document.getElementById("lisenBtn")
    let output = document.getElementById("output");
    let currentSubs = localStorage.getItem("transcribe");

    if (currentSubs){
      output.value = currentSubs
    }
    
    lisenBtn.addEventListener("click", ()=>{
      fetch('http://localhost:5000/play_audio', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: output.value })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Ошибка сети: ' + response.status);
        }
        return response.blob();
      })
      .then(audioBlob  => {
        console.log(audioBlob);
        console.log(audioBlob.type);
        const audioUrl = URL.createObjectURL(audioBlob);
        const audio = new Audio(audioUrl);
        audio.play();
        
      })
      .catch(error => {
        console.error('Произошла ошибка при отправке:', error);
      });
    })

    button.addEventListener("click", () => {
        const textToSend = input.value.trim();

        if (!textToSend || !textToSend.includes("youtube.com") && !textToSend.includes("twitch.tv")){
            output.value = "Link not found. This extentions only handles links from twitch.tv or youtube.com"
        }else{
          output.value = "Transcribing..."


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
            output.value = data.message;
            localStorage.setItem("transcribe", data.message);
            // Очистить поле ввода после успешной отправки
            if (data.status === 'success') {
                input.value = '';
            }
          })
          .catch(error => {
            sendResultDiv.textContent = 'Ошибка: ' + error.message;
            console.error('Произошла ошибка при отправке:', error);
          });
        }
        
    });
});
