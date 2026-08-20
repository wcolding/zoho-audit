from matcher.Matcher import *

def get_report_row(template: str, entry: dict) -> str:
    row = template.replace("%%ENTRY_DISPLAY_NAME%%", entry['Display Name'])
    row = row.replace("%%ENTRY_MAS_ID%%", entry['CF.MASID'])
    row = row.replace("%%ENTRY_ZOHO_ID%%", entry['Contact Address ID'])
    return row

def get_group_report(template: str, group: dict) -> str:
    group_report_full = template.replace("%%REPORT_HEADER%%", f"{group[0]} - {len(group[1])} hits")
    group_report_sections = group_report_full.split("%%REPORT_ENTRY%%")
    group_report = group_report_sections[0]
    for matched_entry in group[1]:
        cur_report_row = get_report_row(group_report_sections[1], matched_entry)
        group_report += cur_report_row
    group_report += group_report_sections[2]
    return group_report

def get_report_content(template: str, matcher: Matcher) -> str:
    sections = template.split("%%REPORT_SECTION%%")
    pre_reports_section = sections[0].replace("%%REPORT_CONTENT_ID%%", matcher.name) \
        .replace("%%REPORT_CONTENT_HEADER%%", f"By {matcher.name} - {len(matcher.matched.keys())} results")
    reports_section = sections[1]
    post_reports_sections = sections[2]

    content = pre_reports_section

    for group in matcher.matched.items():
        cur_group_report = get_group_report(reports_section, group)
        content += cur_group_report

    content += post_reports_sections
    return content

def generate_report_HTML(email_matcher: EmailMatcher, phone_matcher: PhoneMatcher, name_matcher:NameMatcher):
    html_template = open("template/report_template.html", "r")
    html_data = html_template.read()
    html_template.close()

    css_file = open("template/report.css", "r")
    css_data = css_file.read()
    css_file.close()
    html_data = html_data.replace("%%STYLE_SECTION%%", css_data)

    js_file = open("template/report.js", "r")
    js_data = js_file.read()
    js_file.close()
    html_data = html_data.replace("%%SCRIPT_SECTION%%", js_data)

    template_sections = html_data.split("%%REPORT_CONTENT_SECTION%%")
    pre_content_section = template_sections[0]
    content_section = template_sections[1]
    post_content_section = template_sections[2]

    output_file = open("report.html", "w+")
    output_file.write(pre_content_section)

    if email_matcher:
        content = get_report_content(content_section, email_matcher)
        output_file.write(content)

    if phone_matcher:
        content = get_report_content(content_section, phone_matcher)
        output_file.write(content)

    if name_matcher:
        content = get_report_content(content_section, name_matcher)
        output_file.write(content)

    output_file.write(post_content_section)
    output_file.close()