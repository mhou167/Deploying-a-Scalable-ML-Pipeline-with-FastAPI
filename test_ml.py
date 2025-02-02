import pytest
# TODO: add necessary import
from ml.model import train_model, inference
from train_model import data, test
from ml.data import process_data


# TODO: implement the first test. Change the function name and input as needed
def test_column_count():
    """
    # This test is to confirm the correct number of columns.
    """
    # Your code here
    assert 15 == data.shape[1]

    #pass


# TODO: implement the second test. Change the function name and input as needed
def test_column_names():
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
    #pass


# TODO: implement the third test. Change the function name and input as needed
def test_data_type():
    """
    #This test will assure the process step transformed column 0 to binary.
    """
    # Your code here
    assert data['salary'].dtype == object
    #pass
