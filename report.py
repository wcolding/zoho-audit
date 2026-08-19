def GenerateReportHTML(matches: dict):
    html_template = open("report_template.html", "r")
    html_data = html_template.read()
    html_template.close()

    template_sections = html_data.split("%%REPORT_SECTION%%")
    pre_report_section = template_sections[0]
    report_section = template_sections[1]
    post_report_section = template_sections[2]

    output_file = open("report.html", "w+")
    output_file.write(pre_report_section)

    for match_group in matches.keys():
        cur_report = report_section.replace("%%REPORT_HEADER%%", f"{match_group} - {len(matches[match_group])} hits")
        cur_report_sections = cur_report.split("%%REPORT_ENTRY%%")
        output_file.write(cur_report_sections[0])
        for matched_entry in matches[match_group]:
            cur_report_row = cur_report_sections[1].replace("%%ENTRY_DISPLAY_NAME%%", matched_entry['Display Name'])
            cur_report_row = cur_report_row.replace("%%ENTRY_MAS_ID%%", matched_entry['CF.MASID'])
            cur_report_row = cur_report_row.replace("%%ENTRY_ZOHO_ID%%", matched_entry['Contact Address ID'])
            output_file.write(cur_report_row)
        output_file.write(cur_report_sections[2])

    output_file.write(post_report_section)
    output_file.close()
        

