const unitConverter = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yard: 0.9144,
    inch: 0.0254
};

const ft = 0.3048
const mi = 1609.34
const m = 1
const km = (m * 1000)
const yard = .9144
const inch = .0254
let inputUnit = prompt("What is the distance?");
let startingUnit = prompt("What is the conversion units you'd like to start with? ft, yard, inch, mi, m, or km?")
let askUnit = prompt("What units would you like to convert? ft, yard, inch, mi, m, or km?");
let outPutUnit = unitConverter[askUnit] * Number(inputUnit);
alert(Number(inputUnit) + askUnit + " is " + outPutUnit + " meters ")