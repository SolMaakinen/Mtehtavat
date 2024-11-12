function addParticipants() {
    const count = parseInt(document.getElementById('participantCount').value);
    if (count > 0) {
        const form = document.getElementById('participantForm');
        const inputs = document.getElementById('participantInputs');
        inputs.innerHTML = ''; // Clear previous inputs
        for (let i = 0; i < count; i++) {
            const input = document.createElement('input');
            input.type = 'text';
            input.placeholder = `Participant ${i + 1}`;
            input.id = `participant${i}`;
            inputs.appendChild(input);
        }
        form.style.display = 'block';
    }
}

function displayParticipants() {
    const inputs = document.querySelectorAll('#participantInputs input');
    const names = Array.from(inputs).map(input => input.value).sort();
    const list = document.getElementById('participantList');
    list.innerHTML = ''; // Clear previous list
    names.forEach(name => {
        const li = document.createElement('li');
        li.textContent = name;
        list.appendChild(li);
    });
}
