import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--files', nargs='*', help='File(s) to include')
parser.add_argument('-e', '--email', help='Check contacts for overlapping emails')
args = parser.parse_args()

master_list = list()

def MatchEmails(contacts: list):
    emails = dict()
    matched = dict()
    fields = ['EmailID', 'CF.Accounting Email']
    for contact in contacts:
        new_emails = dict()
        for field in fields:
            contact_email = contact[field]
            if contact_email not in new_emails.keys() and contact_email.strip():
                new_emails[contact_email] = contact
        
        for new_email in new_emails:
            if new_email in emails.keys():
                if new_email not in matched.keys():
                    matched[new_email] = [emails[new_email], new_emails[new_email]]
                else:
                    matched[new_email].append(new_emails[new_email])

        emails |= new_emails
            
    print("The following emails were matched:\n")
    for match in matched.keys():
        print(f"  {match} - {len(matched[match])} hits")
        for entry in matched[match]:
            print(f"    Name: {entry['Display Name']} | MASID: {entry['CF.MASID']} | Zoho ID: {entry['Contact Address ID']}")
        print("--------------------")
        

for file in args.__dict__['files']:
    print(f'File requested: {file}')
    file = open(file, "r")
    file_dict = csv.DictReader(file)
    for row in file_dict:
        master_list.append(row)
    file.close()

#MatchEmails(master_list[0:100])