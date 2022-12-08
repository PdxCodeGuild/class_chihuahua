const conversion = { 
    ft : 0.3048,
    mi : 1609.34,
    m : 1,
    km : 1000,
    yd : 0.9144,
    in : 0.0254
}


function converter(){
    let input1 = parseInt(prompt('Please input a number'))
    let input2 = prompt('Please choose the unit type(ft, mi, m, km, yd or in)')
    let input3 = prompt('Please choose the output unit (ft, mi, m, km, yd or in)')

    let meters = input1 * conversion[input2]

    let convertedDistance = meters/conversion[input3]

    console.log(convertedDistance)


    //if (input2 == 'ft')
    //    return console.log(input1 * conversion.ft);
    //else if (input2 == 'mi')
    //     return console.log(input1 * conversion.mi);
    // else if (input2 == 'm')
    //     return console.log(input1 * conversion.m);
    // else if (input2 == 'km')
    //     return console.log(input1 * conversion.km);
    // else if (input2 == 'yd')
    //     return console.log(input1 * conversion.yd);
    // else if (input2 == 'in')
    //     return console.log(input1 * conversion.in);
    
    
    }



console.log(converter())

    
