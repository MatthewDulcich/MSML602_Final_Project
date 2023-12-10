from serpapi import GoogleSearch
import json
from urllib.parse import parse_qsl, urlsplit
import pandas as pd
import os
from secret_key import API_KEY
# from google.colab import files

data_filepath = '../data'
params = {
    'api_key': API_KEY,  # Replace with your actual API key
    'engine': 'google_play',    # SerpApi search engine
    'store': 'apps'             # Google Play Apps
}
 
search = GoogleSearch(params)
result_dict = search.get_dict()
 
# Print the entire response to analyze its structure
print(json.dumps(result_dict, indent=2, ensure_ascii=False))
 
# Check for the presence of 'organic_results' key
if 'organic_results' in result_dict:
    google_play_apps = result_dict['organic_results']
    print(json.dumps(google_play_apps, indent=2, ensure_ascii=False))
else:
    print("No organic results found in the response.")
 
def scrape_apps_from_all_pages(params):
    # params = {
    #     'api_key': API_KEY,  # Replace with your actual API key
    #     'engine': 'google_play',    # SerpApi search engine
    #     'store': 'apps'             # Google Play Apps
    # }
 
    search = GoogleSearch(params)
    apps = []
 
    while True:
        # get updated information from next page
        results = search.get_dict()
 
        if 'error' in results:
            print(results['error'])
            break
 
        # Check for the presence of 'organic_results' key
        if 'organic_results' in results:
            for app in results['organic_results']:
                items = app.get('items', [])
                apps.extend(items)
 
            if 'next' in results.get('serpapi_pagination', {}):
                search.params_dict.update(dict(parse_qsl(urlsplit(results.get('serpapi_pagination', {}).get('next')).query)))
            else:
                break
        else:
            print("No organic results found in the response.")
            break
 
    return apps
 
# Get the list of apps
apps_data = scrape_apps_from_all_pages(params)
key_vs_value = dict()
for record in apps_data:
    # if(record not in set) :
    #     set.add(record)
    if(record['title'] not in key_vs_value):
        key_vs_value[record['title']] = record
 

apps_data = []
 
# for val in apps_data:
 
for key in key_vs_value:
    apps_data.append(key_vs_value.get(key))
 
# Convert the list of dictionaries into a pandas DataFrame
df = pd.json_normalize(apps_data)
 
# Save the DataFrame to a CSV file
csv_filename = 'google_play_apps.csv'
csv_file = df.to_csv(csv_filename, index=False)
 
# Download the CSV file to your local system
# Check if the folder exists, if not, create it
if not os.path.exists(data_filepath):
    os.makedirs(data_filepath)

# Define the file path within the data folder
file_path = os.path.join(data_filepath, csv_filename)

# Write data to the file
with open(file_path, 'w') as file:
    file.write(csv_file)