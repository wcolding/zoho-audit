import argparse
import csv
from matcher.Matcher import *

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--files', nargs='*', help='File(s) to include')
parser.add_argument('-e', '--email', action="store_true", help='Check contacts for overlapping emails')
args = parser.parse_args()

master_list = list()

for file in args.files:
    print(f"Reading file '{file}'")
    file = open(file, "r")
    file_dict = csv.DictReader(file)
    for row in file_dict:
        master_list.append(row)
    file.close()

if args.email:
    email_matcher = EmailMatcher()
    email_matcher.find_matches(master_list)
    report = email_matcher.get_report()
    report_file = open("report.txt", "w+")
    report_file.write(report)
    report_file.close()
    print("Wrote report to 'report.txt'")