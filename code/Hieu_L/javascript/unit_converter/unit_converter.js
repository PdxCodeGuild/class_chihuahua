function convert_from_feet(valNum) {
    document.getElementById("number_in_meters").value = valNum/3.2808;
    document.getElementById("number_in_miles").value = valNum*0.00018939;
    document.getElementById("number_in_kilometers").value = valNum/3280.8;
    document.getElementById("number_in_inches").value = valNum*12;
}

function convert_from_meters(valNum) {
    document.getElementById("number_in_feet").value = valNum*3.2808;
    document.getElementById("number_in_miles").value = valNum*0.00062137;
    document.getElementById("number_in_kilometers").value = valNum/1000;
    document.getElementById("number_in_inches").value = valNum*39.370;
}

function convert_from_kilometers(valNum) {
    document.getElementById("number_in_meters").value = valNum*1000;
    document.getElementById("number_in_miles").value = valNum*0.62137;
    document.getElementById("number_in_feet").value = valNum*3280.8;
    document.getElementById("number_in_inches").value = valNum*39370;
}

function convert_from_miles(valNum) {
    document.getElementById("number_in_meters").value = valNum/0.00062137;
    document.getElementById("number_in_feet").value = valNum*5280;
    document.getElementById("number_in_kilometers").value = valNum/0.62137;
    document.getElementById("number_in_inches").value = valNum*63360;
}

function convert_from_inches(valNum) {
    document.getElementById("number_in_meters").value = valNum/39.370;
    document.getElementById("number_in_miles").value = valNum*0.000015783;
    document.getElementById("number_in_kilometers").value = valNum/39370;
    document.getElementById("number_in_feet").value = valNum*0.083333;
}