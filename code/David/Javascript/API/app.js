const para = document.getElementById('joke')

fetch('https://api.chucknorris.io/jokes/random')
  .then(response => response.json())
  .then(data => console.log(data['value']))
  para.appendChild(data['value'])
  .catch(error => console.log(error))