import pandas
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinnamon_data = len(data[data["Primary Fur Color"] == "Cinnamon"])
balck_data = len(data[data["Primary Fur Color"] == "Black"])
gray_data = len(data[data["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_data, balck_data, cinnamon_data]
}

df = pandas.DataFrame(data_dict)

df.to_csv('Squirrel.csv', index=False)

