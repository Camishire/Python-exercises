import pandas
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrel)

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrel_count)
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrel_count)
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")