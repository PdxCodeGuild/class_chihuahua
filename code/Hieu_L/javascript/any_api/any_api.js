var button = document.getElementById("submit_button")
// let zip_code = document.querySelector("text")

button.addEventListener("click", function (event) {
    let zip_code = document.querySelector("input").value;
    fetch(`https://api.openweathermap.org/data/2.5/weather?zip=${zip_code}&appid=eedc48688c60bb57fc72a154f84d724c`)
        .then(function (response) {
            return response.json()
        }).then(function(data) {
            change_weather(data)
            console.log(data)
        });
})
    .catch(function (error) {
        console.log(error)
    })

function change_weather(data) {
    let weather = data.weather[0]['main'];
    let weather_display = document.getElementById('main_weather');
    weather_display.innerHTML = weather;
    let real_temperature = data.main['temp'];
    let the_temperature = document.getElementById("temp_selector");
    the_temperature.innerHTML = real_temperature;
    let city = data.name;
    let name = document.getElementById("name");
    name.innerHTML = city;
}
