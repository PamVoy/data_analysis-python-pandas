import pandas as pd
import openpyxl
import csv

data = pd.read_csv("data_01.csv")

print(data.shape)

data_installs_sum = data["Installs"].sum()

print("Total install results : ",data_installs_sum)
# print(data.columns)
# print(data.shape)

data['Installs_sum'] = data_installs_sum

data.to_excel("data_ex01.xlsx",encoding="cp950")
