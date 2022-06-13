import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

df = pd.read_csv('stone.csv')
print(df)

df["label"] = df["label"].str.lower()       # normalize each name of the label
df["label"] = df["label"].str.title()       # capitalize the first character of the name
df.loc[df["label"] == "Agate\\", "label"] = "Agate"     # edit name with extra special characters

df = df.sort_values(["label"], ascending = True)    # sort all entries by their names

print("\nprint gemstones' types and their count:\n")
print(df.loc[:, "label"].value_counts())

df = df.groupby('label').filter(lambda x : len(x) > 100)    # drop all rows that have label names' frequencies less than 100

print("\n\n\nUnique Labels: \n")
print(pd.unique(df["label"]))       # print out all unique labels in the data frame

print("\nDescribe the data: \n")
print(df.describe())        # data statistics
df.to_csv("finalcsv.csv", index = False)    # save to the new csv file

plt.hist(df['label'] , bins = 100)
plt.ylabel('Frequency count', rotation='vertical')
plt.xlabel('Data')
plt.title('Frequency histogram')
plt.xticks(rotation='vertical', fontsize=8)
plt.show()