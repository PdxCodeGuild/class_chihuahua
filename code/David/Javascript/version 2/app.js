let base_unit = prompt('Which unit do you want to start with ')
let quant = prompt('How many')

const units = {
    ft : 0.3048,
    mi : 1609.34,
    m : 1,
    km : 1000,

}

let convert = units[base_unit] * quant

console.log(convert)