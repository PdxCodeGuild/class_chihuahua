const measurementConversion = {
    ft:.3048,
    mi:1609.34,
    m:1,
    km:1000
};

let measurementInput = prompt("What are the units to convert? (ft, mi, m, km): ");
    measurementInput = parseFloat(measurementConversion[measurementInput])

let measurementValue = prompt("What is the value to be converted into meters?: ")
    measurementValue = parseFloat(measurementValue)

let output = measurementInput * measurementValue;
alert(output)

