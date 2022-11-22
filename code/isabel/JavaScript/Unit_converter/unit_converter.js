const unit_converter = {
    ask_user: function(){
        alert('Enter a number to be converted from feet to meters:  ')
    },
    convertFeetToMeters() {
        return unit_converter.ask_user * 0.3048
    },
    answerAskUser() {
        return `${unit_converter.ask_user} feet is ${unit_converter.convertFeetToMeters()} meters.`
    }
}