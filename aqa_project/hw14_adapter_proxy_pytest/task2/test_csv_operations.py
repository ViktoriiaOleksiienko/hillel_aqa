import pytest
from hw14_adapter_proxy_pytest.task2 import csv_operations
import csv


@pytest.fixture
def csv_filename(tmp_path):
    filename = tmp_path / "test.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["first_name", "last_name", "age", "gender", "salary"])
        writer.writerow(["Elizabet", "Fork", "19", "Female", "3000"])
        writer.writerow(["Reginald", "Lidoo", "42", "Male", "2500"])
        writer.writerow(["Alexander", "Great", "30", "Male", "15000"])
    return filename


def test_add_row_to_csv(csv_filename):
    new_row = ["John", "Doe", "25", "Male", "5000"]
    csv_operations.add_row_to_csv(csv_filename, new_row)

    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert len(rows) == 5


def test_delete_row_from_csv(csv_filename):
    row_index_to_delete = 1
    csv_operations.delete_row_from_csv(csv_filename, row_index_to_delete)

    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert len(rows) == 3

