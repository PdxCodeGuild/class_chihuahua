const btn = document.getElementById('btn')
const numberTrivia = document.getElementById('numberInput')
let banner = document.getElementById('banner')
let qualityBanner = document.getElementById('quality')

btn.addEventListener('click', function () {
    const number = numberTrivia.value
    if (number == '') {
        return
    }
    // getData(number)
    results = getData(number)
    console.log(results, "testing response")

    })

    function getData(number) {
        fetch(`http://numbersapi.com/${number}/trivia`) // ${}
            .then(function (response) {
                console.log(response, "testing response")
                return response.text()
            })
            .then(function (data) {
                console.log(data, "test")
                const div = document.querySelector("#test")
                div.innerHTML = data
                return data
            })
            .catch(function (error) {
                console.log(error)
                return error
            })

    }
    let input = document.getElementById("numberInput");
        console.log(numberInput)
    let btn1 = document.getElementById("btn");
    test = document.querySelector("#numberInput");
    test.innerHTML = "test";
    btn1.addEventListener("click", function(){
        console.log("hello")
        console.log(input.value)
    })
    
    