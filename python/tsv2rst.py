#! /usr/bin/env python

"""
Convenience script to transform a TSV file (with headers) into an RST table
TSV input on STDIN, eg. tsv_to_rst_table.py < my_table.tsv
"""

import sys, csv

def add_padding(item, col_width):
    pad = col_width - len(item)
    return item+' '*pad

rows = []
max_widths = []
# first pass to read input and find column widths
reader = csv.reader(sys.stdin, delimiter="\t")
for row in reader:
    rows.append(row)
    if len(max_widths) == 0:
        max_widths = [0]*len(row)
    for i in range(len(row)):
        if max_widths[i] < len(row[i]):
            max_widths[i] = len(row[i])
# second pass to print output
divider = ' '.join(['='*w for w in max_widths])
print(divider)
print(' '.join([add_padding(rows[0][i], max_widths[i]) for i in range(len(rows[0]))]))
print(divider)
for i in range(1, len(rows)):
    cells = []
    for j in range(len(rows[i])):
        cells.append(add_padding(rows[i][j], max_widths[j]))
    print(' '.join(cells))
print(divider)
