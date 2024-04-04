from kursovay_account_transactions.utils import loading_file, filter_list, sorts_date, changes_date_format, get_hide_num, get_format_summa, get_main
import os
from config import ROOT_DIR
import pytest

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
    {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
    {"id": 4, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001"}
]
@pytest.fixture
def operations_fixture():
    return operations

test_path = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
def test_loading_file():
    assert loading_file(test_path) == []

def test_filter_list(operations_fixture):
    assert len(filter_list(operations_fixture)) == 3

def test_sorts_date(operations_fixture):
    assert [i["id"] for i in sorts_date(operations_fixture)] == [3, 2, 4, 1]

def test_changes_date_format():
    assert changes_date_format("2018-01-01T00:00:00.000000") == "01.01.2018"

def test_get_hide_num():
    assert get_hide_num("Visa Classic 7756673469642839") == "Visa Classic 7756 67** **** 2839"
    assert get_hide_num("Счет 43597982997568165086") == "Счет **5086"


