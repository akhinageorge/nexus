const searchForm = document.getElementById('search-form');
const cardSection = document.getElementById('card-section');

// Listen for form submission
searchForm.addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent the form from submitting (to demonstrate the card section)

    // Create an example card
    const card = document.createElement('div');
    card.classList.add('card');

    // Bus details
    const busName = document.createElement('h3');
    busName.textContent = 'Bus Name: BusX';

    const startingPoint = document.createElement('p');
    startingPoint.textContent = 'Starting Point: Point A';

    const endingPoint = document.createElement('p');
    endingPoint.textContent = 'Ending Point: Point B';

    const source = document.createElement('p');
    source.textContent = 'Source: Point A';

    const destination = document.createElement('p');
    destination.textContent = 'Destination: Point B';

    const totalTime = document.createElement('p');
    totalTime.textContent = 'Total Time Taken: 2 hours';

    // Append elements to the card
    card.appendChild(busName);
    card.appendChild(startingPoint);
    card.appendChild(endingPoint);
    card.appendChild(source);
    card.appendChild(destination);
    card.appendChild(totalTime);

    // Append the card to the card section
    cardSection.appendChild(card);

    // Show the card section
    cardSection.style.display = 'block';

    // Reset the form (you can modify this to clear the input fields)
    searchForm.reset();
});