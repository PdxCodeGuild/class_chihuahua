const unit_converter = {
    ask_user: function(){
        prompt('Enter a number to be converted from feet to meters:  ')
    },
    convertFeetToMeters() {
        return unit_converter.ask_user * 0.3048
    },
    answerAskUser() {
        return `${unit_converter.ask_user[0]} feet is ${unit_converter.convertFeetToMeters()} meters.`
    }
}

console.log(unit_converter.answerAskUser())