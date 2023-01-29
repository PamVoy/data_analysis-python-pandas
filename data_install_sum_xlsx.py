import pandas as pd
import openpyxl
import csv

data = pd.read_csv("data_01.csv")

print(data.shape)

print(data)

print(data.columns)

# data.drop(['Unnamed: 0'],axis=1,inplace=True)

data.pop('Unnamed: 0')

print(data)

print(data.shape)

# data.to_csv("data_01.csv",encoding="cp950")

# data.to_excel("data_ex01.xlsx",encoding="cp950")

data.to_csv("data_01.csv",encoding="utf-8")

# print(data["Installs"])

# data_installs_sum = data["Installs"].sum()

# print("Total install results : ",data_installs_sum)

############################

# data_to_append = [ 0, 0, 0, 0, 0,data_installs_sum, 0, 0, 0, 0, 0, 0, 0 ]

# file = open( 'data_01.csv' , 'a', newline='') 

# writer = csv.writer(file)

# writer.writerows(data_to_append)

# file.close()

# data = pd.read_csv("data_01.csv")

# data.to_excel("data_ex01.xlsx",encoding="cp950")

data = pd.read_csv("data_01.csv")

# print(data.shape)

# print(data)

# print(data.columns)

# new_row = [0,0,0,0,0,0,1,0,0,0,0,0,0,0]

# columns_list = list(data.columns) 

# new_index = [data.shape[0]]

# print(new_row)

# print(columns_list)

# add_data = pd.DataFrame(new_row, new_index, columns_list)

# print(add_data)

# print(add_data.shape)

data_installs_sum = data["Installs"].sum()

data_to_append = [ [data.shape[0], 0, 0, 0, 0, 0,data_installs_sum, 0, 0, 0, 0, 0, 0, 0] ]

file = open( 'data_01.csv' , 'a', newline='') 

writer = csv.writer(file)

writer.writerows(data_to_append)

file.close()

data = pd.read_csv("data_01.csv")

data.to_excel("data_ex01.xlsx",encoding="cp950")
