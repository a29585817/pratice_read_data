temper = []
with open("weather_data.csv", "r") as f:
    data = csv.reader(f)
    for row in data:
        if row[1] != "temp":
            row[1] = int(row[1])
            temper.append(row[1])

print(temper)


data = pd.read_csv("weather_data.csv")
print(data["temp"])

data_temp_list = data["temp"].to_list()
average = data["temp"].mean()
max = data["temp"].max()
print(data_temp_list)
print(average)
print(max)
data_dict = data.to_dict()
print(data_dict)

#Get Data in row

print(data[data.temp == data["temp"].max()])
monday = data[data.day == "Monday"]

mon_temp = monday.temp
print(mon_temp)
print(mon_temp * 9/5 + 32)
