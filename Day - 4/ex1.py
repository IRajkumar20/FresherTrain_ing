import pandas as pd

s1=pd.read_csv('ex1.csv')

print("----------------------max----------------------------------------")

print("max_salary:", s1["salary"].max())

print("----------------------min--------------------------------------")

print("min_salary:", s1["salary"].min())

print("----------------------sum----------------------------------------")

print("total_salary:", s1["salary"].sum())

print("----------------------unique & count----------------------------------------")

print("total_id:",pd.DataFrame(s1["name"].unique()).count())

print("----------------------mean----------------------------------------")

print("avg_salary:",s1["salary"].mean())

print("----------------------row & column----------------------------------------")

print(s1.iloc[:4,:3])

print("---------------------------is null-----------------------------------")

print(s1[s1.location.isnull()])

print("-----------------------regex---------------------------------------")

print(s1[s1.email.str.contains("@yahoo.com")])

print("-------------------number range-------------------------------------------")

print(s1[s1["salary"].between(10000,30000)])