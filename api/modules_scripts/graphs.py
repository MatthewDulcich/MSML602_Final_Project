'''
graphing script to plot the data and save it as a picture to be loaded on the webpage
'''
import matplotlib.pyplot as plt
import mpld3
import os
import pandas as pd

def load_data():
    data_filepath = '../data'

    # Load the DataFrame from a CSV file
    csv_filename = 'google_play_apps.csv'

    # Define the file path within the data folder
    file_path = os.path.join(data_filepath, csv_filename)

        # Read the CSV file into a pandas DataFrame
    return pd.read_csv(file_path)

def plot_histogram():
    
    df = load_data()

    # Extracting app ratings from the search results
    ratings = df['rating']
    
    # Plotting a histogram
    fig, ax = plt.subplots()
    plt.hist(ratings, bins=5, edgecolor='black')
    plt.xlabel('Ratings')
    plt.ylabel('Frequency')
    plt.title('Distribution of Google Play App Ratings')
    #plt.show()
    interactive_plot = mpld3.fig_to_html(fig)

    with open('../webpage/interactive_plot.html', 'w') as file:
        file.write(interactive_plot)

def plot_pie_chart():

    df = load_data()


    # 'category' is available in the app data
    categories = df['category']
    
    # Counting the occurrences of each category
    category_counts = {category: categories.count(category) for category in set(categories)}
    
    # Setting a larger figure size
    plt.figure(figsize=(8, 10))
    
    # Plotting a pie chart
    plt.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Google Play App Categories')
    plt.show()

def plot_download_data():
    print('hi')


if __name__ == "__main__":
    plot_histogram()