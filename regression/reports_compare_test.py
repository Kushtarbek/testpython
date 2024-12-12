import pytest
import csv

# def testlogin():
#     print("login success")
#
# def testlogoff():
#     print("logoff success")
#
# def testcalc():
#     assert 2+2 == 4
#
# def testlogin1():
#         print("login success")
#
# def testlogoff2():
#         print("logoff success")
@pytest.mark.skip #sanity regression
def testcalc2():
        assert 2 + 2 == 4


def read_data_from_csv(filename):
    datalist = []

    csvdata = open(filename, "r")
    reader = csv.reader(csvdata)
    next(reader)

    for rows in reader:
        datalist.append(rows)
    return datalist


