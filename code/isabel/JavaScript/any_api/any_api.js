fetch('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
    .then(function (response) {
        return response.json()
    }).then(function (data) {
        document.getElementById("image").src = data.hdurl
        
    })
    .catch(function (error) {
        console.log(error)
    })

fetch(data)
