const measurementConversion = {
    ft:.3048,
    mi:1609.34,
    m:1,
    km:1000,
    yd:.9144,
    in:.0254
};

let measurementInput = prompt("What are the input units? (ft, mi, m, km, yd, in): ");
    measurementInput = parseFloat(measurementConversion[measurementInput])

let measurementOutput = prompt("What are the output units?: (ft, mi, m, km, yd, in): ")
    measurementOutput = parseFloat(measurementConversion[measurementOutput])

let measurementValue = prompt("What is the value to be converted?: ")
    measurementValue = parseFloat(measurementValue)

    alert("The input units entered: " + measurementInput + "The output units entered: " + measurementOutput + ". The value entered: " + measurementValue)
    
let output = (measurementValue * measurementInput)/measurementOutput;
alert(output)

// > what is the distance? 100
// > what are the input units? ft
// > what are the output units? mi
// 100 ft is 0.0189394 mi