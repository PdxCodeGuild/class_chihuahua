var button = document.getElementById("information")

button.addEventListener("click", function (event) {
    fetch('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
        .then(function (response) {
            return response.json()
        }).then(function (data) {

            //write asynchronous code here

        })
        .catch(function (error) {
            console.log(error)
        })
})
