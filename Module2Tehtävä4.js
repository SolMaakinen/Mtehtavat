const numbers = [];

function addNumber() {
    const number = parseInt(document.getElementById('numberInput').value);
    if (number === 0) {
        numbers.sort((a, b) => b - a);
        console.log('Numbers in Descending Order:', numbers);
    } else {
        numbers.push(number);
    }
    document.getElementById('numberInput').value = ''; // Clear input field
}
