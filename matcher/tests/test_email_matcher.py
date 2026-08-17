import pytest
import csv
from matcher.Matcher import EmailMatcher

# Populate test data
test_data = list()
file = open("matcher/tests/test_contacts.csv", "r")
file_dict = csv.DictReader(file)
for row in file_dict:
    test_data.append(row)
file.close()

matcher = EmailMatcher()
matcher.find_matches(test_data)

def test_total_number_matched():
    assert len(matcher.matched) == 3

def test_case_insensitive_entries():
    assert len(matcher.matched["unclejesse34@yahoo.com"]) == 3