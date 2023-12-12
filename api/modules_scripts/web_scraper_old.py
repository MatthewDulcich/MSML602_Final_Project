# echo "John, 30, New York" >> sample.csv
# echo "Alice, 25, San Francisco" >> sample.csv
'''
Deprecated: do not use
Test file until real web_scraper.py was made
'''
import os
import csv

def main():
    folder_name = "../data"

    # Create a folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, "data.csv")

    data = [
        {"Name": "Alice", "Age": 25},
        {"Name": "Bob", "Age": 30},
        {"Name": "Charlie", "Age": 35}
    ]

    # Writing data to CSV file
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ["Name", "Age"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data
        for person in data:
            writer.writerow(person)

    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    main()
