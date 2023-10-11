
import pytest

from searchEngine.csvSearch import searchCsvFile

# Define test cases using parametrization
@pytest.mark.parametrize(
    'keyword, column, sortingOrder, expectedResult', [
        ('keyword', 'existingColumn', 'ascending', ['result1', 'result2']),   # Test case 1
        ('keyword', 'nonExistingColumn', 'ascending', []),                    # Test case 2
        # Add more test cases as needed
    ]
)
def test_searchCsvFile(keyword, column, sortingOrder, expectedResult):
    # Act: Call the function to be tested
    result = searchCsvFile(keyword, column, sortingOrder)

    # Assert: Check the expected outcome
    assert result == expectedResult


if __name__ == '__main__':
    pytest.main()






