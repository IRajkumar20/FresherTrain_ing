import csv

header= ['name','id','admission_date']
data=[['raj',1,'13/11/2001'],['kumar',12,'11/11/2002'],['ram',3,'19/12/2001'],['sakthi',4,'11/12/2002'],['karthi',5,'01/03/2003']]

file_name= input("enter file name:")

with open(file_name,"w") as file:
    for i in header:
        file.write(str(i) + " ,")
    file.write("\n")

    for j in data:
        for x in j:
            file.write(str(x) + " ,")
        file.write("\n")


