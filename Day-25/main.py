"""import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)"""

"""import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

print(data["temp"].mean())

print(data["temp"].max())

print(data.condition)

print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(monday_temp)
monday_temp_F = monday_temp * 9/5 +32
print(monday_temp_F)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
student_data = pandas.DataFrame(data_dict)
print(student_data)
student_data.to_csv("new_student_data")"""

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")