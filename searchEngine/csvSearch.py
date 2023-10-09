
import csv
import os

def searchCsvFile(keyword, column):
    """Search for data from the csv file"""
    fileLocation = os.path.join('csvFolder', 'anime.csv')

    matchingData = []

    with open(fileLocation, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Check if the column name exists in the CSV file's headers
        if column not in reader.fieldnames:
            return matchingData  # Return an empty list if the column doesn't exist

        for row in reader:
            if keyword.lower() in row[column].lower():
                matchingData.append(row[column])

    return matchingData

# results = searchCsvFile('Naruto', 'title')
# 
# for row in results:
    # print(row)






