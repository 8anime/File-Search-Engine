
import csv
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # Obtain the directory in which the 'csvSearch.py' is located
ROOTDIR = os.path.dirname(SCRIPT_DIR)                    # Obtain the directory of searchEngine folder
CSV_FOLDER = 'csvFolder'                                 # Name of directory containing the csv files to be read from
FILE = 'anime.csv'                                       # Name of the file to read from

fileLocation = os.path.join(ROOTDIR, CSV_FOLDER, FILE)

def searchCsvFile(keyword, column, sortingOrder='ascending'):
    """Search for data from the csv file"""
    matchingData = []  # Stores returned values from the csv

    with open(fileLocation, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Check if the column name exists in the CSV file's headers
        if column not in reader.fieldnames:
            return matchingData  # Return an empty list if the column doesn't exist

        for row in reader:  # 'row' is treated like a dictionary
            # Check if a keyword value exists in the value returned from a row
            if keyword.lower() in row[column].lower():  # 'column' is the key that retrieves a value(s) from the row(dictionary)
                matchingData.append(row[column])        # Add the value to 'matchingData' list if a keyword value exists in it

    # Apply sorting based on the sortingOrder parameter
    if sortingOrder == 'ascending':
        matchingData.sort()               # Sort in ascending order by default
    elif sortingOrder == 'descending':
        matchingData.sort(reverse=True)   # 'reverse=True' makes it sort in descending order

    return matchingData

# results = searchCsvFile('Naruto', 'title')
# 
# for row in results:
    # print(row)






