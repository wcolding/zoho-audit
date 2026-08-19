import argparse
import csv
from matcher.Matcher import *
from report import GenerateReportHTML

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

if args.email:
    email_matcher = EmailMatcher()
    email_matcher.find_matches(master_list)
    GenerateReportHTML(email_matcher.matched)
    


if args.phone:
    phone_matcher = PhoneMatcher()
    phone_matcher.find_matches(master_list)
    report = phone_matcher.get_report()
    report_file = open("phone_report.txt", "w+")
    report_file.write(report)
    report_file.close()
    print("Wrote report to 'phone_report.txt'")

if args.name:
    name_matcher = NameMatcher()
    name_matcher.find_matches(master_list)
    report = name_matcher.get_report()
    report_file = open("name_report.txt", "w+")
    report_file.write(report)
    report_file.close()
    print("Wrote report to 'name_report.txt'")