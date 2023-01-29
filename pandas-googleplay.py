import pandas as pd
import openpyxl

## access data
data = pd.read_csv("googleplaystore.csv")
## csv => dataframe
## observe data
# print(data)
# print(data.shape)   # data amount

# print(data.columns)  # data columns name

# print("===============================")

# print(data["Rating"]) # observe columns "Rating"

# condition = data["Rating"] > 5  # find error data
# data = data[condition]
# print(data)

# condition = data["Rating"] <= 5
# data = data[condition]
# print("平均數:",data["Rating"].mean())
# print("中位數:",data["Rating"].median())
# print("top1000 APP的平均數:",data["Rating"].nlargest(1000).mean())

############################################################### 

# print("平均數:",data["Installs"].mean())  # observe data columns "Install" mean

# print(data["Installs"])  # observe data columns "Install"

# data["Installs"] = pd.to_numeric(data["Installs"]) # string to number
## debug srting "10,000" : ',' and '+'

# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","")) 
## string to number & replace ',' '+'

## fail , ValueError: Unable to parse string "Free" at position 10472

# print(data["Installs"][10472])

## data["Installs"][10472] dispaly 'Free'

data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
# ## string to number & replace ',' '+' 'Free'

##print(data["Installs"])
# ## object => float64

# print("平均數:",data["Installs"].mean())  # observe data columns "Install" mean

# condition = data["Installs"] > 100000
# result = data[condition]
# amount_row_colu = result.shape
# ##print(amount_row_colu)
# amount = amount_row_colu[0]
# print("安裝數 > 100k 的APP個數:", amount)

############################################################### 

## 使用關鍵字搜尋APP

keyword = input("Please type keyword : ")
# condition = data["App"].str.contains(keyword) # keyword大小寫會造成影響
# print(data[condition])  # too much information

condition = data["App"].str.contains(keyword, case=False)  # keyword大小寫,忽略


print(data[condition].columns)

# print(data[condition]["App"])

print(data[condition])

result = data[condition]
amount_row_colu = result.shape
print(amount_row_colu)
amount = amount_row_colu[0]

print("包含 " ,keyword, " 的APP數量 : ", amount)

# data.to_excel("data_01.xlsx",encoding="cp950")

# data.to_csv("data_01.csv",encoding="cp950")

# data.to_csv("data_01.csv",encoding="utf-8")

filter_data = data[condition]

# filter_data.to_csv("data_01.csv",encoding="cp950")

filter_data.to_csv("data_01.csv",encoding="utf-8")
