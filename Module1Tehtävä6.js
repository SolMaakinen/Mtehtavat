if (confirm("Should I calculate the square root?")) {
  const number = parseFloat(prompt("Enter a number:"));
  const output = document.getElementById("output");

  if (number < 0) {
    output.textContent = "The square root of a negative number is not defined.";
  } else {
    const squareRoot = Math.sqrt(number);
    output.textContent = `The square root of ${number} is ${squareRoot}`;
  }
} else {
  document.getElementById(
      "output").textContent = "The square root is not calculated.";
}