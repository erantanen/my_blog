#! /usr/bin/env python


import openpyxl
import socket


def create_workbook():
    wb = openpyxl.Workbook()
    return wb


def create_worksheet(wb, sheet_name):
    work_page = wb.create_chartsheet(sheet_name)
    return work_page


def data_to_worksheet(wb, data):
    print("blah")
    ws = wb.worksheets[0]
    ws['A1'] = data


def save_workbook(wb, file_name):
    wb.save(filename=file_name)


def main():
    # configs
    workbook_name = "dink.xlsx"
    work_sheet_name = "data_1"

    # fake data?
    gobbledygook = socket.gethostname()

    # working code
    wb = create_workbook()
    ws = create_worksheet(wb, work_sheet_name)

    data_to_worksheet(wb, gobbledygook)
    save_workbook(wb, workbook_name)


if __name__ == "__main__":
    main()