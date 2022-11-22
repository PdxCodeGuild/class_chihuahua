/*const unit_converter = {
    ask_user: function(){
        let user_number = Number(prompt('Enter a number to be converted from feet to meters:  '))
        return user_number
    },
    convertFeetToMeters() {
        return unit_converter.ask_user * 0.3048
    },
    answerAskUser() {
        return `${unit_converter.ask_user[0]} feet is ${unit_converter.convertFeetToMeters()} meters.`
    }
}

console.log(unit_converter.ask_user[0])
console.log(unit_converter.answerAskUser())
*/

const unit_converter = {
    askUser(){
        let user_number = Number(prompt('Enter a number to be converted from feet to meters:  '))
        return user_number
    },
    convertFeetToMeters() {
        return unit_converter.askUser * 0.3048
    },
    answerAskUser() {
        return `${unit_converter.askUser} feet is ${unit_converter.convertFeetToMeters()} meters.`
    }
}

console.log(unit_converter.askUser())
console.log(unit_converter.answerAskUser())

