window.addEventListener('message', function(event) {
    const item = event.data;
    const watchContainer = document.getElementById('watch-container');

    switch (item.action) {
        case 'show':
            watchContainer.style.display = 'block';
            break;

        case 'hide':
            watchContainer.style.display = 'none';
            break;

        case 'updateHud':
            // Update the text values for each stat
            updateStatValue('health', item.stats.health);
            updateStatValue('armor', item.stats.armor);
            updateStatValue('stamina', item.stats.stamina);
            updateStatValue('hunger', item.stats.hunger);
            updateStatValue('thirst', item.stats.thirst);
            updateStatValue('hygiene', item.stats.hygiene);
            updateStatValue('radioactivity', item.stats.radioactivity);
            updateStatValue('infection', item.stats.infection);
            break;
    }
});

function updateStatValue(stat, value) {
    const element = document.getElementById(`${stat}-value`);
    if (element) {
        element.innerText = Math.floor(value);
    }
}

// For browser testing:
// document.getElementById('watch-container').style.display = 'block';
// updateStatValue('health', 80);
// updateStatValue('infection', 25);
