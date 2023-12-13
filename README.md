# MSML602_Final_Project
Data Science Final Project | UMD | MSML602 | 2023

# App Store App Predictor

This project aims to predict the success of an app on the App Store using machine learning techniques. The data for this project is scraped from [Google Play Store](https://play.google.com/store/apps?hl=en_US&gl=US) and utilizes Python 3.10.12, scikit-learn, selenium, and SerpApi, along with a hosted Docker container running Flask with uwsgi and nginx.

## Overview

The goal of this project is to develop a predictive model that can forecast the performance of an app based on various features such as user ratings, category, and more. By leveraging scraped data from the Google Play Store, we aim to build a robust model that can assist app developers in understanding the factors contributing to an app's success on the App Store.

## Dataset

The dataset used in this project is scraped from the Google Play Store. It contains various apps available on the store.

## Methodology

1. **Data Collection:** Scraping data from the Google Play Store using google-play-scraper, selenium, google-search-results, and SerpApi.
2. **Data Preprocessing:** Cleaning, feature extraction, and transformation of the scraped data.
3. **Model Development:** Utilizing random forest regressor to train and evaluate the predictive model.
4. **Deployment:** Hosting the model in a Docker container with Flask, uWSGI, and NGINX to provide a web service for app prediction.

## Dependencies

- Python 3.10.12
- Libraries: Found in requirements.txt

## Usage

1. **Clone Repository:**
    ```
    git clone https://github.com/MatthewDulcich/MSML602_Final_Project.git
    ```

2. **Setting Up:**
    - Ensure Python 3.10.12 is installed.
    - Ensure pip is installed.
    - If you are one windows and you cannot run on a linux backend, comment out uwsgi from the requirements.txt file.
    - Ensure Docker is installed and running.
    - Activate or create a conda environment or python venv.
    - Install required libraries:
    ```
    pip install -r requirements.txt
    ```
    - Make file named secret_key.py
    ```
    # Add this line of code, you can sign up for a API key at https://serpapi.com

    API_KEY = "SerpApiKey"
    ```
    
    

3. **Running the Flask App:**
    - Build and run the Docker container:
    ```
    docker compose up --build
    ```
    - Access the Flask app at `http://localhost`.

## Results

[Include visualizations or summary of key findings/results here]

## Future Improvements

- Fine-tuning model hyperparameters for better accuracy using more data over time.
- Improving the user interface.
- Host the web app online.

## Contributors

- [Matthew Dulcich](https://github.com/MatthewDulcich)
- [Yajat Uppal](https://github.com/Agenzmain)
- [Neelagriri Keerthi Kaushik](https://github.com/NK-Kaushik)

## Acknowledgments

- Google Play Scraper
- SerpApi

## License

This project is not licensed.
