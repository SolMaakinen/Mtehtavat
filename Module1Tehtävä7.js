const rolls = parseInt(prompt("How many dice would you like to roll?"));
let sumRolls = 0;

for (let i = 0; i < rolls; i++) {
  sumRolls += Math.floor(Math.random() * 6) + 1;
}

document.getElementById("output").textContent = `Sum of ${rolls} dice rolls is ${sumRolls}`;
