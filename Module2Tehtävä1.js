function displayReverse() {
    // Get input values
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const num3 = document.getElementById('num3').value;
    const num4 = document.getElementById('num4').value;
    const num5 = document.getElementById('num5').value;

    // Store them in an array
    const numbers = [num1, num2, num3, num4, num5];

    // Display numbers in reverse order
    const reverseNumbers = [];
    for (let i = numbers.length - 1; i >= 0; i--) {
        reverseNumbers.push(numbers[i]);
    }

    // Output to the result div
    document.getElementById('result').innerText = reverseNumbers.join(', ');
}
