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
