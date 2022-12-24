function convert() {
    const inputValue = document.getElementById("inputValue").value;
    const inputUnit = document.getElementById("inputUnit").value;
    let outputValue;
  
    if (inputUnit === "feet") {
      outputValue = inputValue * 0.3048;
    } else if (inputUnit === "miles") {
      outputValue = inputValue * 1609.34;
    } else if (inputUnit === "kilometers") {
      outputValue = inputValue * 1000;
    } else if (inputUnit === "yards") {
      outputValue = inputValue * 0.9144;
    } else if (inputUnit === "inches") {
      outputValue = inputValue * 0.0254;
    }
  
    document.getElementById("outputValue").textContent = outputValue;
  }
  