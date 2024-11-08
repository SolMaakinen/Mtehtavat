const year = parseInt(prompt("Enter a year:"));

const isLeapYear = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
document.getElementById("output").textContent = `${year} is ${isLeapYear ? "a leap year" : "not a leap year"}.`;
