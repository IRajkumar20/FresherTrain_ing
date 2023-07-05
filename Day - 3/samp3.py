import pandas as pd

s1=pd.read_csv("emp1.csv")
s2=pd.read_csv("emp2.csv")

s3=pd.merge(s1,s2 ,how="left")

s4=s3.groupby(["id","emp_name","emp_area"])["salary"].mean()

s4.to_csv("avg_final.csv")
