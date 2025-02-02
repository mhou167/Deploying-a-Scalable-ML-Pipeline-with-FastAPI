import pytest
# TODO: add necessary import
from train_model import data


# TODO: implement the first test. Change the function name and input as needed
def test_column_count(data):
    """
    # This test is to confirm the correct number of columns.
    """
    # Your code here
    assert 15 == data.shape[0]

    pass


# TODO: implement the second test. Change the function name and input as needed
def test_column_names(data):
    """
    # This test will ensure the columns match expected columns.
    """
    # Your code here
    expected_colums = [
        "age",
        "workclass",
        "fnlgt",
        "education",
        "education-num",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital-gain",
        "capital-loss",
        "hours-per-week",
        "native-country",
        "salary",
    ]

    these_columns = data.columns.values

    # This also enforces the same order
    assert list(expected_colums) == list(these_columns)
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_binary(data):
    """
    #This test will assure the process step transformed column 0 to binary.
    """
    # Your code here
    my_test = data['salary'].isin([0,1]).all()
    assert my_test, "Test failed: Not all values in the salary column are binary"
    print("Test passed: all values in the salary column are binary")
    pass
