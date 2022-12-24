// console.log('about to fetch a space picher');
// fetch('https://api.nasa.gov/planetary/apod?api_key=wtBOUoGpVmhQLQpvp7jzr710d9ulsQEf96JScu5d')
//     .then(function (response) {
//         return response.json()
//     }).then(function (data) {

//         //write asynchronous code here
//         async function fetchText() {
//             let response = await fetch('https://api.nasa.gov/planetary/apod?api_key=wtBOUoGpVmhQLQpvp7jzr710d9ulsQEf96JScu5d');
//             let data = await response.text();
//             console.log(data);
//         }

//     })
//     .catch(function (error) {
//         console.log(error)
//     })

const newpic = document.querySelector("#space")
console.log(newpic)
fetch('https://api.nasa.gov/planetary/apod?api_key=wtBOUoGpVmhQLQpvp7jzr710d9ulsQEf96JScu5d')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        
        async function fetchText() {
            let response = await fetch('https://api.nasa.gov/planetary/apod?api_key=wtBOUoGpVmhQLQpvp7jzr710d9ulsQEf96JScu5d');
            let data = await response.json();
            newpic.src = data.hdurl
            console.log(data);
        }

        
        fetchText();
    })
    .catch(function (error) {
        console.log(error);
    });
