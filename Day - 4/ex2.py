# Comprehension List, Aggregation using Lambda.


num=int(input("enter the number of area:"))
area=[]

print("enter ur " + str(num) + " areas: ")
for i in range(num):
   area.append(input())

char=input("enter one char: ")

identify= lambda name,char : [i for i in area if char not in i]

print(identify(area,char))