const studentName = prompt("Enter your name:");
const house = Math.floor(Math.random() * 4) + 1;

let houseName;
switch (house) {
  case 1:
    houseName = "Gryffindor";
    break;
  case 2:
    houseName = "Slytherin";
    break;
  case 3:
    houseName = "Hufflepuff";
    break;
  case 4:
    houseName = "Ravenclaw";
    break;
}

document.getElementById("output").textContent = `${studentName}, you are ${houseName}.`;
