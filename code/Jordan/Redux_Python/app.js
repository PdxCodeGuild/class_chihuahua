const unitConverter = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yard: 0.9144,
    inch: 0.0254
};

let inputUnit = prompt("What is the distance?");
let startingUnit = prompt("What is the conversion units you'd like to start with? Choose either ft, yard, inch, mi, m, or km.");
let askUnit = prompt("What units would you like to convert to? ft, yard, inch, mi, m, or km?");
if (startingUnit == askUnit) {
    outPutUnit = inputUnit;
}
else {
    distanceMeters = unitConverter[startingUnit] * Number(inputUnit);
    outPutUnit = Math.round(distanceMeters / unitConverter[askUnit]);
}
alert(Number(inputUnit) + startingUnit + " is " + outPutUnit + askUnit)

// function idea
// if startingUnit == askUnit {
//  let outPutUnit = startingUnit
// }
// else {
//  outPutUnit = unitConverter[askUnit] * Number(inputUnit);    
// }
//                  return startingUnit
//                  else if unitConverter[askUnit] * Number(inputUnit);
// let outPutUnit = unitConverter[askUnit] * Number(inputUnit);