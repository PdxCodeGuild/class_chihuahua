fetch('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&media_type="image"')
    .then(function (response) {
        return response.json()
    }).then(function (data) {
        console.log(json)
        const dom_manipulation = document.getElementById("image");
        document.getElementById("image").src = data.hdurl
        dom_manipulation.innerHTML = data.media_type;
    
        //write asynchronous code here

    })
    .catch(function (error) {
        console.log(error)
    })

fetch(data)
