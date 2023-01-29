import pandas as pd
import openpyxl
import csv

data = pd.read_csv("googleplaystore.csv")

data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))

total_installs_sum = data["Installs"].sum()

print('total installs sum : ',total_installs_sum)

keyword = 'game'
# game

# communication

# tools

condition = data["Category"].str.contains(keyword, case=False)

print(data[condition])

filter_data = data[condition]

data_installs_sum = filter_data["Installs"].sum()

print(keyword ,'installs sum : ', data_installs_sum)

Category_game_installs_sum = data_installs_sum

###########################################################################

keyword = 'communication'

condition = data["Category"].str.contains(keyword, case=False)

print(data[condition])

filter_data = data[condition]

data_installs_sum = filter_data["Installs"].sum()

print(keyword ,'installs sum : ', data_installs_sum)

Category_communication_installs_sum = data_installs_sum

###########################################################################

keyword = 'tools'

condition = data["Category"].str.contains(keyword, case=False)

print(data[condition])

filter_data = data[condition]

data_installs_sum = filter_data["Installs"].sum()

print(keyword ,'installs sum : ', data_installs_sum)

Category_tools_installs_sum = data_installs_sum

##########################################################

total_installs_sum
game_sum = Category_game_installs_sum
communication_sum = Category_communication_installs_sum
tools_sum = Category_tools_installs_sum

game_percent = (game_sum / total_installs_sum) * 100
communication_percent = (communication_sum / total_installs_sum) * 100
tools_percent = (tools_sum / total_installs_sum) * 100

print('game_installs : ', game_percent, '%')
print('communication_installs : ', communication_percent, '%')
print('tools_installs : ', tools_percent, '%')

# obser_data = [  [ game_sum, communication_sum, tools_sum, total_installs_sum ],
#                 [ game_percent, communication_percent, tools_percent, 100 ]
# ]

obser_data = [  [ game_sum, game_percent ],
                [ communication_sum, communication_percent ],
                [ tools_sum, tools_percent ],
                [ total_installs_sum, 100 ]
]

# indexs = [ "installs sum", "  installs sum / total installs  (%)" ]
# columns= [ "game", "communication", "tools", "total installs"]

indexs = [ "game", "communication", "tools", "total installs"]
columns = [ "installs sum", "  installs sum / total installs  (%)" ]

df = pd.DataFrame(obser_data, indexs, columns)
df.to_excel("installs_analysis_01.xlsx",encoding="cp950")



