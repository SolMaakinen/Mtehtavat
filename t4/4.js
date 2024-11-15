'use strict';
// Array of students with their IDs and names
const students = [
    { id: '2345768', name: 'John' },
    { id: '2134657', name: 'Paul' },
    { id: '5423679', name: 'Jones' }
];

// Get the target element
const target = document.getElementById('target');

// Loop through the students array
for (let i = 0; i < students.length; i++) {
    // Create a new <option> element
    const option = document.createElement('option');
    // Set the value attribute
    option.value = students[i].id;
    // Set the text content
    option.textContent = students[i].name;
    // Append the <option> element to the target
    target.appendChild(option);
}