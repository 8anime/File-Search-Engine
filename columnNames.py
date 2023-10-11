
# THE PURPOSE OF THIS FILE IS TO KNOW THE COLUMNS THAT ARE AVAILABLE IN THE CSV FILE.
# THIS FILE WILL RETRIEVE THE COLUMNS FROM THE CSV FILE. THE COLUMN NAMES ARE CASE-SENSITIVE.
# ASSUMING EVERYTHING IS SET UP CORRECTLY, RUN THE FILE DIRECTLY WITHOUT CHANGING ANYTHING EXCEPT IF YOU WANT TO USE A DIFFERENT CSV FILE.

# Import necessary libraries
import os
import csv

ROOTDIR = '.\\'
FOLDER = 'csvFolder'
FILE = 'anime.csv'  # update this part to your desired csv file

# Define the file location of the CSV file to be read
fileLocation = os.path.join(ROOTDIR, FOLDER, FILE)

def csvReader():
    """Read a csv file"""
    # Open the CSV file for reading with specified encoding
    with open(fileLocation, 'r', encoding='utf-8') as file:
        # Create a CSV reader object that treats the first row as column names
        reader = csv.DictReader(file)
    
        # Get the column names from the CSV file
        columns = reader.fieldnames
    
        # Print the column names
        print(columns)

csvReader()














