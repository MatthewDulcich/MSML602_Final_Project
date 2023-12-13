'''
preprocessing, pipeline, and load pickled file
'''
import pandas as pd
import numpy as np
import os

# Test function
def predict_pipeline(sample):
    return {'text': 'test text', 'pred': int(0), 'label': 'cat?'}

def preprocessing():

    data_filepath = '../data'

    # Load the DataFrame to a CSV file
    csv_filename = 'google_play_apps.csv'

    # Define the file path within the data folder
    file_path = os.path.join(data_filepath, csv_filename)

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    df.drop(columns = ['serpapi_link','thumbnail','video','images','link','title','description','product_id'], inplace=True)

    df = df.drop_duplicates()

    df['downloads'] = df['downloads'].str.replace("+", "")
    df['downloads'] = df['downloads'].str.replace(",", "")

    df.downloads = pd.to_numeric(df['downloads'])

    # X = df.drop("rating", axis=1)
    # y = df["rating"]

    # X = pd.get_dummies(X[["author","category","downloads"]])

    # X['downloads'] = X['downloads'] / X['downloads'].max()

    # Save the DataFrame to a CSV file
    csv_filename = 'google_play_apps_cleaned.csv'
    # Define the file path within the data folder
    file_path = os.path.join(data_filepath, csv_filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        
    df.to_csv(file_path, index=False)




if __name__ == "__main__":
     preprocessing()