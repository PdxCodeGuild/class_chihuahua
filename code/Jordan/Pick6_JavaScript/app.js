// function to create the winning numbers
const ticket = 6;
const winningNumbers = [];
const earnings = {
    0:0,
    1:4, 
    2:7, 
    3:100, 
    4:50000, 
    5:1000000, 
    6:25000000
};

function pick6() {
    let randomSix = []
    for(let index = 0; index < 6; index += 1) {
        randomSix.push(Math.floor(Math.random()*10)) // multiply by 10 to make it a whole number
    }
//console.log(randomSix)
return randomSix
};
console.log(pick6())