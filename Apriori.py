from efficient_apriori import apriori
import pandas as pd
import xlrd
import csv

with xlrd.open_workbook('Base de dados.xls') as wb:
    sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
    with open('Base de dados.csv', 'wb') as f:   # open('a_file.csv', 'w', newline="") for python 3
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))


""" transactions = [('eggs', 'bacon', 'soup'),
                ('eggs', 'bacon', 'apple'),
                ('soup', 'bacon', 'banana')]
itemsets, rules = apriori(transactions, min_support=0.5,  min_confidence=1)
print(rules)  # [{eggs} -> {bacon}, {soup} -> {bacon}] """

