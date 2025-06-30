import pandas as pd
file_path="a.csv"
df = pd.read_csv(file_path,encoding='utf-8',on_bad_lines="skip")

data = df["Number"].values

if data[1] == "106980095533":
    print(data[1])

# print(df["Source"].values)
