const inputElement = document.getElementById("state");
const buttonElement = document.getElementById("btn");

buttonElement.addEventListener("click", function() {

  const state = inputElement.value;
  const url = "https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest";


  fetch(url)
    .then(function(response) {

      return response.json();
    })
    
    .then(function(data) {
      
      const population = data.data.find(function(x) {
        return x.State === state;
      }).Population;
      
      console.log(population)
      const populationElement = document.getElementById("population");

      populationElement.innerHTML = population;
    })
})
