
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
    QListWidgetItem
)

from csvSearch import searchCsvFile  # Import your search function from csvSearch module


class CSVSearchApp(QMainWindow):
    """The CSVSearchApp is a PyQt5-based desktop application that allows users to search and query data from a CSV file 
    using a user-friendly graphical interface. It provides features for entering search keywords, specifying columns to 
    search in, and displaying search results in a list format. Users can also sort and filter results to quickly find and 
    explore relevant data within the CSV file."""
    def __init__(self):
        super().__init__()

        self.initializeUserInterface()

    def initializeUserInterface(self):
        """Build the user interface of the application"""
        self.setWindowTitle('CSV Search App')  # Window Title
        self.setGeometry(450, 100, 400, 500)   # Set width and height of the window and where on the screen it will appear

        # Determine the arrangement and alignment of the various widgets within the application's main window
        # It is responsible for organizing the widgets in the main window in a vertical orientation from top to bottom
        widgetLayout = QVBoxLayout()

        # Add keyword search box
        self.keywordInput = QLineEdit()           # Input field
        keywordLabel = QLabel('Enter keyword:')   # Input field label
        widgetLayout.addWidget(keywordLabel)      # Add label to the layout
        widgetLayout.addWidget(self.keywordInput) # Add Input field to the layout

        # Add column selection box
        self.columnInput = QLineEdit()                                      # Column input field
        columnLabel = QLabel('Enter columns to search (comma-separated):')  # Column label
        widgetLayout.addWidget(columnLabel)                                 # Add label to the layout
        widgetLayout.addWidget(self.columnInput)                            # Add input field to the layout 

        # Add search button
        searchButton = QPushButton('Search')  # Search button
        widgetLayout.addWidget(searchButton)  # Add search button to the layout

        # Create a QListWidget widget to display search results
        self.resultsDisplay = QListWidget()
        widgetLayout.addWidget(self.resultsDisplay)  # Add widget in the layout

        # Create a dropdown menu that allows users to select sorting category from a list of options
        sortingDropDown = QComboBox()
        sortingDropDown.addItems(['Ascending', 'Descending'])  # Sort search results in ascending and descending order
        widgetLayout.addWidget(sortingDropDown)                # Add widget to the layout

        # Add filter input field
        self.filterInputField = QLineEdit()            # Input field
        widgetLayout.addWidget(self.filterInputField)  # Add widget to the layout
        
        # Add filter button
        filterButton = QPushButton('Filter')  # Filter button
        widgetLayout.addWidget(filterButton)  # Add widget the layout

        # Connect the search button click event to the search function
        searchButton.clicked.connect(self.performSearch) 

        # Connect sorting and filtering controls to functions
        sortingDropDown.currentIndexChanged.connect(self.handleSorting)
        filterButton.clicked.connect(self.handleFilter)

        # Create and set up the main widget
        centralWidget = QWidget()
        centralWidget.setLayout(widgetLayout)

        self.setCentralWidget(centralWidget)

    def performSearch(self):
        searchKeyword = self.keywordInput.text().strip()   # Extract text from the keyword input search box
        columnsToSearch = self.columnInput.text()          # Extract text from the column input search box

        results = searchCsvFile(searchKeyword, columnsToSearch)  # Store the results returned from the function in a variable

        self.resultsDisplay.clear()  # Removes any previously searched results before displaying the new results

        if not results:  # Checks if result is being returned from the function
            item = QListWidgetItem("No matching results found.")  # This is displayed if no result is found
            self.resultsDisplay.addItem(item)                     # Add the display message to the QListWidget view
        else:
            # Display each matching result in the QListWidget view
            for result in results:                 # For every result stored in the results variable
                item = QListWidgetItem(result)     # Create an item object for each result stored in the result variable
                self.resultsDisplay.addItem(item)  # Add each item in the QListWidget view

    def handleSorting(self):
        # Implement sorting logic based on the user's selection
        # Update the displayed data accordingly
        pass

    def handleFilter(self):
        filter_criteria = self.filterInputField.text()
        # Implement filtering logic based on the user's input
        # Update the displayed data to show filtered results
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CSVSearchApp()
    window.show()

    sys.exit(app.exec_())
