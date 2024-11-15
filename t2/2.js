'use strict';
const target = document.getElementById('target');

        // List of items to add
        const items = ['First item', 'Second item', 'Third item'];

        items.forEach(itemText => {
            // Create a new <li> element
            const li = document.createElement('li');
            // Set its text content
            li.textContent = itemText;
            // Append the <li> to the target element
            target.appendChild(li);
        });