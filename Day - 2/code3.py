import csv
import json

csv_path=input("enter csvpath name:")
json_path=input("enter json path:")

json_arr=[]
try:

   
    with open(csv_path,"r") as file1:
       
       csvreader=csv.DictReader(file1)
       for i in csvreader:
           print(i)
           json_arr.append(i)

    with open(json_path,'w') as file2:
        json_string=json.dumps(json_arr,indent=0)
         # print(json_string)
        file2.write(json_string)
        print("csv to json run sucessfully")

except Exception as e:
    print("ERROR " + str(e))


