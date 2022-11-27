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
  askUser: function() {
    let user_number = Number(prompt('Enter a number to be converted:  '))
    return user_number
  },
  askUserStartUnit: function() {
    let start_unit = prompt('Enter START units to be converted in: m, mi, ft, yd, or km:  ')
    return start_unit
  },
  askUserConversion: function() {
    let user_conversion = prompt('Enter END units to convert to in: m, mi, ft, yd, or km:  ')
    return user_conversion
  },
  convertFeetToMeters: function(finalAskUserConversion1) {
    const finalAskUser1 = finalAskUser
    const finalAskUserStartUnit1 = finalAskUserStartUnit
    
    
    if (finalAskUserStartUnit1 === 'ft' && finalAskUserConversion1 === 'm') {
      let conversion = finalAskUser1 * 0.3048
      return conversion
    } else if (finalAskUserStartUnit1 === 'mi' && finalAskUserConversion1 === 'm') {
    let conversion = finalAskUser1 * 1609.34
    return conversion
    } else if (finalAskUserStartUnit1 === 'm' && finalAskUserConversion1 === 'm') {
      let conversion = finalAskUser1 * 1
      return conversion
    } else if (finalAskUserStartUnit1 === 'km' && finalAskUserConversion1 === 'm') {
      let conversion = finalAskUser1 * 1000
      return conversion
    } else if (finalAskUserStartUnit1 === 'ft' && finalAskUserConversion1 === 'mi') {
      let conversion = finalAskUser1 * 0.000189394
      return conversion
    } else if (finalAskUserStartUnit1 === 'ft' && finalAskUserConversion1 === 'km') {
      let conversion = finalAskUser1 * 0.0003048
      return conversion
    } else if (finalAskUserStartUnit1 === 'mi' && finalAskUserConversion1 === 'mi') {
      let conversion = finalAskUser1 * 1
      return conversion
    } else if (finalAskUserStartUnit1 === 'ft' && finalAskUserConversion1 === 'ft') {
      let conversion = finalAskUser1 * 1
      return conversion 
    } else if (finalAskUserStartUnit1 === 'km' && finalAskUserConversion1 === 'km') {
      let conversion = finalAskUser1 * 1
      return conversion 
    } else if (finalAskUserStartUnit1 === 'mi' && finalAskUserConversion1 === 'km') {
      let conversion = finalAskUser1 * 1.60934
      return conversion
    } else if (finalAskUserStartUnit1 === 'km' && finalAskUserConversion1 === 'mi') {
      let conversion = finalAskUser1 / 1.60934

    } else if (finalAskUserStartUnit1 === 'km' && finalAskUserConversion1 === 'ft') {
      let conversion = finalAskUser1 / 0.0003048
      return conversion

    } else if (finalAskUserStartUnit1 === 'mi' && finalAskUserConversion1 === 'ft') {
      let conversion = finalAskUser1 / 0.000189394
      return conversion
    } else if (finalAskUserStartUnit1 === 'm' && finalAskUserConversion1 === 'km') {
      let conversion = finalAskUser1 / 1000
      return conversion
    } else if (finalAskUserStartUnit1 === 'm' && finalAskUserConversion1 === 'mi') {
    let conversion = finalAskUser1 / 1609.34
    return conversion
    } else if (finalAskUserStartUnit1 === 'm' && finalAskUserConversion1 === 'ft') {
      let conversion = finalAskUser1 / 0.3048
      return conversion
    }


  },
  answerAskUser: function(finalAskUser, finalAskUserStartUnit,finalAskUserConversion1) {
  const finalConvertFeetToMeters = unit_converter.convertFeetToMeters(finalAskUserConversion1)

    return `${finalAskUser} ${finalAskUserStartUnit} is ${finalConvertFeetToMeters} ${finalAskUserConversion1}.`
  }
}

const finalAskUser = unit_converter.askUser()
const finalAskUserStartUnit = unit_converter.askUserStartUnit()

let finalAskUserConversion = unit_converter.askUserConversion()

console.log(unit_converter.answerAskUser(finalAskUser, finalAskUserStartUnit, finalAskUserConversion))





