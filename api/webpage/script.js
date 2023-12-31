// script.js
console.log("Hello from script.js! This script is running.");

function showDataView() {
    // Get the main content area
    const mainContent = document.querySelector('.main-content');

    // Fetch data from the server
    fetch('/display')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            // Set the fetched data into the #dataTable element
            const dataTable = document.getElementById('dataTable');
            if (dataTable) {
                dataTable.innerHTML = data;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });

    // Set or load the initial content into the main content area
    mainContent.innerHTML = '<div id="dataTable"></div>';
}

function showAnalysisView() {

    // Get the main content area
    const mainContent = document.querySelector('.main-content');

     // Fetch the HTML file content using Fetch API
     fetch('/graphing')
     .then(response => response.text())
     .then(data => {
         // Display the fetched HTML content in the 'html-content' div
         mainContent.innerHTML = data;
     })
     .catch(error => console.error('Error fetching HTML:', error));
    //  mainContent.innerHTML = '<div id="dataTable"></div>';
}


    // // var interactivePlot = document.getElementById('interactive-plot');
    // // // Paste the generated mpld3 plot HTML here
    // // interactivePlot.innerHTML = `<div id="interactive-plot"></div>`;

    // // Get the main content area
    // const mainContent = document.querySelector('.main-content');

    // // Fetch data from the server
    // fetch('/graph')
    //     .then(response => {
    //         if (!response.ok) {
    //             throw new Error('Network response was not ok');
    //         }
    //         return response.text();
    //     })
    //     .then(data => {
    //         // Set the fetched data into the #dataTable element
    //         const interactive_plot = document.getElementById('interactive-plot');
    //         if (interactive_plot) {
    //             interactive_plot.innerHTML = data;
    //             // Initialize mpld3 plot
    //             mpld3.draw_figure('interactive-plot', eval(interactive_plot.textContent));
    //         }
    //     })
    //     .catch(error => {
    //         console.error('Error:', error);
    //     });

    // // Set or load the initial content into the main content area
    // mainContent.innerHTML = '<div id="interactive-plot"></div>';
// }




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
        //document.getElementById('response').innerText = JSON.stringify(data, null, 2);
        return data;
    })
    .catch(error => {
        console.error('There was a problem with the POST request:', error);
    });
}

function showPostData() {
    const mainContent = document.querySelector('.main-content');
    mainContent.innerHTML = '<h2>POST View</h2><p>This is the POST view content.</p> <div id="response"></div>';

    const dataToSend = { text: 'input test text' };
    // postData('http://127.0.0.1:5001/predict', dataToSend)
    postData('http://127.0.0.1/predict', dataToSend)
        .then(data => {
            // console.log(data)

            // document.addEventListener('DOMContentLoaded', function() {
                // Your code here
         
            // Clear previous content in the response area
            const responseElement = document.getElementById('response');
            // console.log(responseElement)
            responseElement.innerHTML = "";

            // Create elements to display the response data
            const labelHeading = document.createElement('h2');
            labelHeading.textContent = 'Label: ' + (data.label ? data.label : 'Not available');

            const predParagraph = document.createElement('p');
            predParagraph.textContent = 'Prediction: ' + (data.pred !== undefined ? data.pred : 'Not available');

            const textParagraph = document.createElement('p');
            textParagraph.textContent = 'Text: ' + (data.text ? data.text : 'Not available');

            // Append the elements to the response area
            responseElement.appendChild(labelHeading);
            responseElement.appendChild(predParagraph);
            responseElement.appendChild(textParagraph);
        // });
        })
        .catch(error => {
            console.error('There was a problem with the showPostData request:', error);
        });
}
