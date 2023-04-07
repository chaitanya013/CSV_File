import csv
import pandas as pd

with open(r"C:\Users\DELL\Videos\python programs\NewFile.csv",'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
df = pd.read_csv(r"C:\Users\DELL\Videos\python programs\NewFile.csv")
print(df)