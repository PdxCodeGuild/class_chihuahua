const btn = document.getElementById('btn')
const numberTrivia = document.getElementById('numberInput')
let banner = document.getElementById('banner')
let qualityBanner = document.getElementById('quality')

btn.addEventListener('click', function () {
    const number = numberTrivia.value
    if (number == '') {
        return
    }
    getData(number)

    })

    function getData(number) {
        fetch(`http://numbersapi.com/${number}/trivia`) // ${}
            .then(function (response) {
                console.log(response)
                return response.text()
            })
            .then(function (data) {
                console.log(data)
            })
            .catch(function (error) {
                console.log(error)
                return error
            })

    }