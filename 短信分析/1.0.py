import pandas as pd
import difflib

df = pd.read_csv("jh.csv", on_bad_lines="skip")

columns = df.columns

print(columns)

# result = df[df['Content'].str.contains('北京')]


# result.to_excel("0422.xlsx")

print(df['Content'])