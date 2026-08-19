import argparse
import csv
from matcher.Matcher import *
from report import generate_report_HTML

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--files', nargs='*', help='File(s) to include')
parser.add_argument('-e', '--email', action="store_true", help='Check contacts for overlapping emails')
parser.add_argument('-p', '--phone', action="store_true", help='Check contacts for overlapping phone numbers')
parser.add_argument('-n', '--name', action="store_true", help='Check contacts for overlapping names')
args = parser.parse_args()

master_list = list()

for file in args.files:
    print(f"Reading file '{file}'")
    file = open(file, "r")
    file_dict = csv.DictReader(file)
    for row in file_dict:
        master_list.append(row)
    file.close()

email_matcher = None
phone_matcher = None
name_matcher = None

if args.email:
    email_matcher = EmailMatcher()
    email_matcher.find_matches(master_list)

if args.phone:
    phone_matcher = PhoneMatcher()
    phone_matcher.find_matches(master_list)

if args.name:
    name_matcher = NameMatcher()
    name_matcher.find_matches(master_list)

generate_report_HTML(email_matcher, phone_matcher, name_matcher)