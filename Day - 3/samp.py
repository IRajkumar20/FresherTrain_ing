import pandas as pd

data1={
    "patient_id":["01","02","03","04","05","06","07","08"],
    "patient_name":["raj","rahul","tharun","kiran","askar","vignesh","thamizh","hari"],
    "token_no":["11","12","13","14","15","16","17","18"],
    "room_no":["101","102","103","104","105","106","107","108"]
}

df=pd.DataFrame(data1)


df.to_csv("sample.csv")