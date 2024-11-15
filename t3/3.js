'use strict';
// Array of names
const names = ['John', 'Paul', 'Jones'];

// Select the target element
const target = document.getElementById('target');

// Initialize an empty string to store the HTML content
let listItems = '';

// Loop through the names array
for (let i = 0; i < names.length; i++) {
    // Add each name as an <li> element to the string
    listItems += `<li>${names[i]}</li>`;
}

// Set the innerHTML of the target element
target.innerHTML = listItems;
