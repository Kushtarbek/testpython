# import inspect
# import logging
# import softtest
# import csv
#
# class Utils(softtest.TestCase):
#
#
#     def read_data_from_excel( file_name, sheet):
#
#         datalist = []
#         wb = load_workbook(filename=file_name)
#
#         sh = wb[sheet]
#         row_ct = sh.max_row
#         col_ct = sh.max_col
#
#         for i in range(2, row_ct + 1):
#             row = []
#             for j in range(1, col_ct + 1):
#                 row.append(sh.cell(row=i, col=j).value)
#             datalist.append(row)
#             return datalist
#
#
#     def read_data_from_csv(filename)
#
#         datalist = []
#         csvdata = open(filename, "r")
#
#         #reader
#         reader = csv.reader(csvdata)
#
#         #skip header
#         next(reader)
#
#         #add csv row to list
#         for rows in reader:
#             datalist.append(rows)
#         return datalist
#
#