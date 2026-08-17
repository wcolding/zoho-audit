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

def test_number_matched():
    matcher = EmailMatcher()
    matcher.find_matches(test_data)
    print(matcher.get_report())
    assert len(matcher.matched) == 3