fetch('https://api.chucknorris.io/')
    .then(function (response) {
        return response.json()
    }).then(function (data) {
        //asynch code here
    })
    .catch(function (error) {
        console.log(error)
    })