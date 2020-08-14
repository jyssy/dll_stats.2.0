# Call_number counts taken from the Monthly DBeaver report for Items

import sys, os, csv

subject_area_counts = {}

with open('cataloging_stats.csv', 'r') as call_stats:
    report_reader = csv.reader(call_stats)
    # skip headers
    next(report_reader)
    for row in report_reader:
        call_num = row[4]

        subject_area = call_num.split('.')[0].strip()
        if subject_area not in subject_area_counts:
            subject_area_counts[subject_area] = 0
        subject_area_counts[subject_area] += 1

    with open('CallNos_out.csv', 'w') as call_stats_report:
        report_writer = csv.writer(call_stats_report)

        for subject_area, count in subject_area_counts.items():
            report_writer.writerow([subject_area, count])

        # RESORT the resulting spreadsheet (manually) so the call numbers are in alpha order.
        # Delete the empty lines (not quite sure how to get rid of that part yet...)
