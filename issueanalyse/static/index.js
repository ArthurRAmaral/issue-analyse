const button = document.getElementById('button');

button.addEventListener("click", sendTextToAnalyse);

function sendTextToAnalyse(event) {
  event.preventDefault();
  const text = document.getElementById("text").value;
  const result = document.getElementById("result");

  let request = new XMLHttpRequest();
  request.open("GET", `/api/analyse/${text}`);
  request.responseType = "json";

  request.onload = function () {
    result.innerHTML = "";

    const isBug = request.response.isBug;
    const textSended = request.response.text;

    result.innerHTML = `É um Bug: ${isBug}<br>Texto enviado: ${textSended}`;
  };

  request.send();
}