# MSML602_Final_Project
Data Science Final Project | UMD | MSML602 | 2023

# App Store App Predictor

This project aims to predict the success of an app on the App Store using machine learning techniques. The data for this project is scraped from [Google Play Store](https://play.google.com/store/apps?hl=en_US&gl=US) and utilizes Python 3.9.18 along with a hosted Docker container running Flask.

## Overview

The goal of this project is to develop a predictive model that can forecast the success or performance of an app based on various features such as user ratings, category, pricing, and more. By leveraging scraped data from the Google Play Store, we aim to build a robust model that can assist app developers in understanding the factors contributing to an app's success on the App Store.

## Dataset

The dataset used in this project is scraped from the Google Play Store. It contains [mention the number of observations and features] and covers various aspects of apps available on the store.

## Methodology

1. **Data Collection:** Scraping data from the Google Play Store using [mention the tools/libraries used].
2. **Data Preprocessing:** Cleaning, feature extraction, and transformation of the scraped data.
3. **Model Development:** Utilizing machine learning algorithms like [list the algorithms used] to train and evaluate the predictive model.
4. **Deployment:** Hosting the model in a Docker container with Flask to provide a web service for app prediction.

## Dependencies

- Python 3.9.18
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Flask, Docker, etc. (Specify versions if necessary)

## Usage

1. **Setting Up:**
    - Ensure Python 3.9.18 is installed.
    - Install required libraries:
    ```
    pip install -r requirements.txt
    ```

2. **Running the Flask App:**
    - Build the Docker container:
    ```
    docker build -t app-predictor .
    ```
    - Run the container:
    ```
    docker run -p 8001:8001 app-predictor
    ```
    - Access the Flask app at `http://localhost:8001`.

## Results

[Include visualizations or summary of key findings/results here]

## Future Improvements

- Fine-tuning model hyperparameters for better accuracy.
- Improving the user interface and experience of the Flask app.

## Contributors

- [Matthew Dulcich](https://github.com/MatthewDulcich)
- [Yajat Uppal](https://github.com/Agenzmain)
- [NK-Kaushik](https://github.com/NK-Kaushik)

## Acknowledgments

- Mention any external sources, tutorials, or repositories referenced in the project.
- google play store scraper name

## License

This project is licensed under [License Name] - see the [LICENSE](LICENSE) file for details.
