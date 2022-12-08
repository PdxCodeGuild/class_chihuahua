const actuallyDisplay = document.querySelector(".actuallyDisplay");
const printData = document.querySelector("#printData");
printData.addEventListener("click", function(event){
    fetch('https://randomuser.me/api/')
.then(function(response){
    return response.json()
})
.then(function(data){
    results = data.results[0]
    console.log(results)
    actuallyDisplay.innerHTML += `<li>${results.gender} Cell phone number: ${results.cell} ${results.name["first"]}</li>`
    paintDom()
})
.catch(function(error){
    return error
})
})