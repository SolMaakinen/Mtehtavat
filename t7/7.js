// Get references to the trigger and target elements
const trigger = document.getElementById('trigger');
const target = document.getElementById('target');

// Event listener for mouseover
trigger.addEventListener('mouseover', () => {
    target.src = 'img/picB.jpg'; // Change the image to picB.jpg
});

// Event listener for mouseout
trigger.addEventListener('mouseout', () => {
    target.src = 'img/picA.jpg'; // Change the image back to picA.jpg
});
