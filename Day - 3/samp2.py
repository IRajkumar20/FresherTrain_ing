import pandas as pd

path1=input("enter first csv file::")
path2=input("enter second csv file::")

s1=pd.read_csv(path1)
s2=pd.read_csv(path2)

s3=pd.merge(s1,s2 ,how="inner")

s3.to_csv("final.csv")