import csv

data={}

with open("employeedet.csv","r") as f1:
    value=csv.DictReader(f1)
    for i in value:
       id = i["id"]
       data[id] = i


index=input("enter index number:")
print(data[index])