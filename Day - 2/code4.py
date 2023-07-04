import csv
with open ("high.csv","w",newline='') as f1:
    w = csv.writer(f1)
    w.writerow(['id','name','age','area'])
    while(True):
        id=input("Enter id number:")
        name=input("Enter ur name:")
        age=int(input("Enter ur age:"))
        area=input("enter ur area:")
        w.writerow([id,name,age,area])
        option=input("yes/no:")
        if option=="no":
            break

with open('high.csv','r') as f1:
    w= csv.DictReader(f1)

    for i in w:
        print(i)
