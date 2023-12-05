// script.js
console.log("Hello from script.js! This script is running.");

function showDataView() {
    // Get the main content area
    const mainContent = document.querySelector('.main-content');

    // Set or load the data view content into the main content area
    mainContent.innerHTML = '<h2>Data View</h2><p>This is the data view content.</p>';
}

function showAnalysisView() {
    // Get the main content area
    const mainContent = document.querySelector('.main-content');

    // Set or load the analysis view content into the main content area
    mainContent.innerHTML = '<h2>Analysis View</h2><p>This is the analysis view content.</p>';
}

function postData(url = '', data = {}) {
    return fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return response.json();
    })
    .then(data => {
        console.log('POST request succeeded with data:', data);
        // Display the response data on the screen
        document.getElementById('response').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('There was a problem with the POST request:', error);
    });
}

document.getElementById('sendButton').addEventListener('click', function() {
    const dataToSend = { text: 'input test text' };
    postData('http://127.0.0.1:8001/predict', dataToSend)
        .then(data => {
            // Handle response data if needed
        });
});