import pandas as pd
import openpyxl
import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(dir_path):
    if filename.lower().endswith((".xlsx")):

        wb = openpyxl.load_workbook(filename)
        sheet = wb["Sheet1"]
        sheet["C6"] = "=SUM(C2:C4)"
        # sheet["C6"].style = "Normal"
        sheet["C6"].style = "Comma"
        wb.save(filename)
