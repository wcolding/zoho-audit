class Matcher():
    master_dict = dict()
    matched = dict()
    name = "Generic"

    def __init__(self):
        self.fields = list()

    def find_matches(self, contacts: list):
        assert len(self.fields) > 0, "No search fields defined! Create a new class that inherits from Matcher and override __init__ to define some"
        for contact in contacts:
                new_entries = dict()
                for field in self.fields:
                    new_key = contact[field].lower()
                    if new_key not in new_entries.keys() and new_key.strip():
                        new_entries[new_key] = contact
                
                for new_entry in new_entries:
                    if new_entry in self.master_dict.keys():
                        if new_entry not in self.matched.keys():
                            self.matched[new_entry] = [self.master_dict[new_entry], new_entries[new_entry]]
                        else:
                            self.matched[new_entry].append(new_entries[new_entry])
        
                self.master_dict |= new_entries

    def get_report(self) -> str:
        num_matches = len(self.matched.keys())
        if num_matches < 1:
             return f"No duplicate entries found with {self.name} matcher using fields {self.fields}"

        report = f"{num_matches} matching entries have been found with {self.name} Matcher:\n\n"
        
        for match in self.matched.keys():
            report += f"{match} - {len(self.matched[match])} hits\n"
            for entry in self.matched[match]:
                report += f"    Name: {entry['Display Name']} | MASID: {entry['CF.MASID']} | Zoho ID: {entry['Contact Address ID']}\n"
            report += "--------------------\n"

        return report

class EmailMatcher(Matcher):
    def __init__(self):
        self.fields = ['EmailID', 'CF.Accounting Email']
        self.name = "Email"