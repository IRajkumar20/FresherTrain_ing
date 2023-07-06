import csv

class employee():
    def __init__(self,id,name,salary,location):
        self.id=id
        self.name=name
        self.salary=salary
        self.location=location

        
list1=[]       

with open("employeedet.csv","r") as f1:
    data=csv.DictReader(f1)
    for i in data:
        value=employee(int(i["id"]),i["name"],int(i["salary"]),i["location"])
        print(value)
        list1.append(value)


for j in list1:
    print(j.id)
    print(j.name)
    print(j.salary)
    print(j.location)
