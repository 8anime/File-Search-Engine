
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QListWidget,
    QListWidgetItem,
    QFileDialog,
    QMessageBox
)


from csvSearch import searchCsvFile  # Import your search function from csvSearch module


class CSVSearchApp(QMainWindow):
    """The CSVSearchApp is a PyQt5-based desktop application that allows users to search and query data from a CSV file 
    using a user-friendly graphical interface. It provides features for entering search keywords, specifying columns to 
    search in and displaying search results in a list format. Users can also sort and save results to quickly find and 
    explore relevant data within the CSV file."""
    def __init__(self):
        super().__init__()

        self.initializeUserInterface()

    def initializeUserInterface(self):
        """Build the user interface of the application"""
        self.setWindowTitle('CSV Search App')  # Window Title
        self.setGeometry(450, 100, 500, 500)   # Set width and height of the window and where on the screen it will appear

        # Determine the arrangement and alignment of the various widgets within the application's main window.
        # It is responsible for organizing the widgets in the main window in a vertical orientation from top to bottom.
        widgetLayout = QVBoxLayout()

        # Add keyword search box
        self.keywordInput = QLineEdit()           # Input field
        keywordLabel = QLabel('Enter keyword:')   # Input field label
        widgetLayout.addWidget(keywordLabel)      # Add label to the layout
        widgetLayout.addWidget(self.keywordInput) # Add Input field to the layout

        # Add column selection box
        self.columnInput = QLineEdit()                                      # Column input field
        columnLabel = QLabel('Enter column to search:')  # Column label
        widgetLayout.addWidget(columnLabel)                                 # Add label to the layout
        widgetLayout.addWidget(self.columnInput)                            # Add input field to the layout 

        # Add search button
        searchButton = QPushButton('Search')  # Search button
        widgetLayout.addWidget(searchButton)  # Add search button to the layout

        # Create a QListWidget view to display search results
        self.resultsDisplayView = QListWidget()
        widgetLayout.addWidget(self.resultsDisplayView)  # Add widget in the layout

        # Create a dropdown menu that allows users to select sorting category from a list of options
        self.sortingDropDown = QComboBox()
        self.sortingDropDown.addItems(['Ascending', 'Descending'])  # Sort search results in ascending or descending order
        widgetLayout.addWidget(self.sortingDropDown)                # Add dropdown menu to the layout

        # Add export button
        saveButton = QPushButton('Save')            # Save button
        widgetLayout.addWidget(saveButton)          # Add save button to the layout

        # Connect the search button click event to the search function
        searchButton.clicked.connect(self.performSearch) 

        # Connect sorting control to function
        self.sortingDropDown.currentIndexChanged.connect(self.handleSorting)

        # Connect export button click event to the exportResults function
        saveButton.clicked.connect(self.saveResults)

        # Create and set up the main widget
        centralWidget = QWidget()
        centralWidget.setLayout(widgetLayout)

        self.setCentralWidget(centralWidget)

    def performSearch(self):
        """Performs a search operation based on user input and displays the results in the QListWidget view."""
        searchKeyword = self.keywordInput.text().strip()   # Extract text from the keyword input search box
        columnsToSearch = self.columnInput.text()          # Extract text from the column input search box

        results = searchCsvFile(searchKeyword, columnsToSearch)  # Store the list returned from the function in a variable

        self.resultsDisplayView.clear()  # Removes any previously searched results before displaying the new results

        if not results:  # Checks if result is being returned from the function
            item = QListWidgetItem("No matching results found.")  # This is displayed if no result is found
            self.resultsDisplayView.addItem(item)                 # Add the display message to the QListWidget view
        else:
            # Display each matching result in the QListWidget view
            for result in results:                     # Loop through the results(List) variable
                item = QListWidgetItem(result)         # Create an item object for each result stored in the result variable
                self.resultsDisplayView.addItem(item)  # Add each item in the QListWidget view

    def handleSorting(self):
        """Implement sorting logic based on the user's selection"""
        # Update the displayed data accordingly
        sortingOrder = self.sortingDropDown.currentText()  # Get text from the combo box

        # Get the current search results from the QListWidget view
        currentResults = [self.resultsDisplayView.item(i).text() for i in range(self.resultsDisplayView.count())]

        if sortingOrder == 'Ascending':           
            currentResults.sort()                 # Ascending by default
        elif sortingOrder == 'Descending':
            currentResults.sort(reverse=True)     # 'reverse=True' makes it descending

        # Clear the current results in the QListWidget view to show sorting results
        self.resultsDisplayView.clear()

        # Display the sorted results in the QListWidget view
        for result in currentResults:               # Loop through the currentResults(List) variable 
            item = QListWidgetItem(result)          # Create an item object for each result stored in the currentResults variable 
            self.resultsDisplayView.addItem(item)   # Add each item in the QListWidget view

    def saveResults(self):
        """Allows users to save and export the obtained results for future reference"""
        # Get the current search results from the QListWidget view
        currentResults = [self.resultsDisplayView.item(i).text() for i in range(self.resultsDisplayView.count())]

        if not currentResults:  # Checks if results have been returned
            return              # No results to save
        
        # Open a file dialog to let the user choose where to save the results
        # Specify various options and flags that control the behaviour and appearance of the file dialog
        options = QFileDialog.Options()  # Control how the file dialog behaves
        # Display a file dialog for saving a file
        filePath, _ = QFileDialog.getSaveFileName(
            # Main window, Title of the file dialog, current directory, Display all files and files with .csv extension and pass the options variable
            self, "Save Results", "", "CSV Files (*.csv);;All Files (*)", options=options
        )

        if filePath:  # Check if filePath exists
            # Write the results to the selected file in CSV format
            try:
                # Write the results to the selected file in CSV format
                with open(filePath, 'w', encoding='utf-8') as file:
                    file.write('\n'.join(currentResults))
                QMessageBox.information(self, "Success", "Results saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while exporting results: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CSVSearchApp()
    window.show()

    sys.exit(app.exec_())
