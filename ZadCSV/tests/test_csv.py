from upload_csv.upload_csv import csv_data
import pytest


@pytest.fixture(scope="module")
def csv_read():
    book = csv_data()
    return book

@pytest.fixture()
def csv_header(csv_read):
    header = csv_read[0]
    return header


def test_headline(csv_header):
    header = csv_header
    assert header == header.upper()


def test_header_starts_with_id(csv_header):
    assert csv_header.startswith("ID")


def test_heder_has_created(csv_header):
    assert "CREATED" in csv_header


def test_heder_has_updated(csv_header):
    assert "UPDATED" in csv_header


def test_number_values(csv_read, csv_header):
    no_headers = len(csv_header.split(","))
    errors = []
    for line in csv_read[1:]:
        if len(line.split(",")) != no_headers:
            errors.append(line)
    assert not errors


def test_first_item_isnumber(csv_read):
    errors = []
    for line in csv_read[1:]:
        if not line.split(",")[0].isdecimal():
            errors.append(line)
    assert not errors











