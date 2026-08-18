import pytest
import csv
from matcher.Matcher import EmailMatcher, PhoneMatcher

# Populate test data
test_data = list()
file = open("matcher/tests/test_contacts.csv", "r")
file_dict = csv.DictReader(file)
for row in file_dict:
    test_data.append(row)
file.close()

class TestEmails:
    em = EmailMatcher()
    em.find_matches(test_data)

    def test_total_number_matched(self):
        assert len(self.em.matched) == 3

    def test_case_insensitive_entries(self):
        assert len(self.em.matched["unclejesse34@yahoo.com"]) == 3


class TestPhoneNumbers:
    pm = PhoneMatcher()
    pm.find_matches(test_data)

    def test_total_number_matched(self):
        assert len(self.pm.matched) == 2