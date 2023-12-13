'''
Code for training the model
'''
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os


def train_model(X, y):
    
    np.random.seed(25)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    model = RandomForestRegressor(n_estimators=17)

    model.fit(X_train, y_train)
    # model.score(X_train,y_train)


    print(model.score(X_test,y_test))
    y_pred = model.predict(X_test)
    print(y_pred)

def load_data():
    data_filepath = '../data'

    # Save the DataFrame to a CSV file
    csv_filename = 'google_play_apps_cleaned.csv'

    # Define the file path within the data folder
    file_path = os.path.join(data_filepath, csv_filename)

        # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    X = df.drop("rating", axis=1)
    y = df["rating"]

    X = pd.get_dummies(X[["author","category","downloads"]])

    X['downloads'] = X['downloads'] / X['downloads'].max()
    
    return X, y

def save_weights(y_pred):
    print('hi')

def save_predict_Xtest(predict, X_test):
    



if __name__ == "__main__":
    X, y = load_data()
    train_model(X, y)