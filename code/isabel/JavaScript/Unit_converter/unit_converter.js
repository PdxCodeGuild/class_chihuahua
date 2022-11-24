// const unit_converter = {
//     askUser() {
//       let user_number = Number(prompt('Enter a number to be converted from feet to meters:  '))
//       return user_number
//     },
//     convertFeetToMeters() {
//       let conversion = unit_converter.askUser() * 0.3048
//       return conversion

//     },
//     answerAskUser() {
//       return `${unit_converter.askUser()} feet is ${unit_converter.convertFeetToMeters()} meters.`
//     }
//   }

//   console.log(unit_converter.answerAskUser())

/*above works for version 1*/


const unit_converter = {
  askUser() {
    let user_number = Number(prompt('Enter a number to be converted:  '))
    return user_number
  },
  askUserStartUnit() {
    let start_unit = prompt('Enter units to be converted in: m, mi, ft, yd, or km:  ')
    return start_unit
  },
  askUserConversion() {
    let user_conversion = prompt('Enter units to convert to in: m, mi, ft, yd, or km:  ')
    return user_conversion
  },
  convertFeetToMeters() {
    if (unit_converter.askUserStartUnit() === 'ft' && unit_converter.askUserConversion() === 'm') {
      let conversion = unit_converter.askUser() * 0.3048
      return conversion
    }
    else if (unit_converter.askUserStartUnit() === 'm' && unit_converter.askUserConversion() === 'ft') {
      let conversion = unit_converter.askUser() / 0.3048
      return conversion
    }

  },
  answerAskUser() {
    return `${unit_converter.askUser()} ${unit_converter.askUserStartUnit} is ${unit_converter.convertFeetToMeters()} ${unit_converter.askUserConversion}.`
  }
}

console.log(unit_converter.answerAskUser())




