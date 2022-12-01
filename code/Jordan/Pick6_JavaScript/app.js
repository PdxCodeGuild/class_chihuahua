function pick6() {
    let randomSix = []
    for(let index = 0; index < 6; index ++) {
        randomSix.push(Math.floor(Math.random()*100)) // multiply by 10 to make it a whole number
    }
    return randomSix
};
//console.log(pick6())

function winnings(winningNumbers, playerNumbers) {
    let matches = 0
    const earnings = {
        0:0,
        1:4, 
        2:7, 
        3:100, 
        4:50000, 
        5:1000000, 
        6:25000000
    };
    for(let index = 0; index < 6; index ++) {
        if (winningNumbers[index] === playerNumbers[index]) {
            matches ++
        }
    }
    return earnings[matches]
}

let winningTicket = pick6()
let playerBalance = 0
let i = 0;
while(i < 100000) {
    let playerTicket = pick6()
    playerBalance -=2 // Balance = Balance -2
    playerBalance += winnings(winningTicket, playerTicket) 
    i++;
}
console.log(playerBalance)