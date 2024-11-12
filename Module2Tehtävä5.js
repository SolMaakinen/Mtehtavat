const uniqueNumbers = new Set();

function addUniqueNumber() {
    const number = parseInt(document.getElementById('uniqueNumberInput').value);
    if (uniqueNumbers.has(number)) {
        const sortedNumbers = Array.from(uniqueNumbers).sort((a, b) => a - b);
        console.log('Unique Numbers in Ascending Order:', sortedNumbers);
    } else {
        uniqueNumbers.add(number);
    }
    document.getElementById('uniqueNumberInput').value = ''; // Clear input field
}
