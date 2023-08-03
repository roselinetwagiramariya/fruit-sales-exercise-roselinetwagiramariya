import os
import pandas as pd
import pytest

CSV_FILE = "fruit.csv"

def test_file_exists():
    assert os.path.exists(CSV_FILE) == True, "csv file does not exist"

def test_columns_exist():
    expected_columns = ['Apples','Bananas']
    try:
        df = pd.read_csv(CSV_FILE)
        for col in expected_columns:
            assert col in df.columns
    except Exception as e:
        assert False, e

@pytest.mark.parametrize("column_name,expected_values",
                        [['Apples', [35,41]],
                        ['Bananas',  [21,34]]
                        ])
def test_values_exist(column_name, expected_values):
    try:
        df = pd.read_csv(CSV_FILE)
        for val in expected_values:
            assert val in df[column_name].values
    except Exception as e:
        assert False, e
