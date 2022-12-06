let myDictionarys = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' :1000,
    'yard' : 0.9144,
    'inch' : 0.0254,
};


let whatIsMyDist = prompt('what is the distance?:  ')
let whatIsMyUnit = prompt('What is my unit of measure')
let whatIsMyOutput = prompt('What are the output units?')



console.log(whatIsMyDist+ " "+whatIsMyUnit+" is " + (Number(whatIsMyDist) * myDictionarys[whatIsMyUnit])/myDictionarys[whatIsMyOutput]+ " " +whatIsMyOutput)

//test//test