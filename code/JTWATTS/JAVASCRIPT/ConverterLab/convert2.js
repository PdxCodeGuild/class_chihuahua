let myDictionary = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' :1000,
};



let whatIsMyDist = prompt('what is the distance?:  ')
let whatIsMyUnit = prompt('What is my unit of measure')



console.log(whatIsMyDist+ " "+whatIsMyUnit+" is " + Number(whatIsMyDist) * myDictionary[whatIsMyUnit]+' m')
//test