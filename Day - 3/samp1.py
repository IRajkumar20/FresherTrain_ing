import pandas as pd

data2={
    "patient_id":["01","02","03","04","05","06","07","08"],
    "location":["chennai","vellore","thirchy","ariyalur","chennai","theni","thiruvellur","chennai"],
    "age":["21","21","22","24","25","36","30","19"],
    "billing":["$1000","$2002","$3000","$4000","$400","$3000","$3500","$2000"]
}

df=pd.DataFrame(data2)

df.to_csv("sample1.csv")