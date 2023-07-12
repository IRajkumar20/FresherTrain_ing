import pandas as p
import numpy as n
import  matplotlib.pyplot as plot
from sklearn import metrics


data1=p.read_csv("ww.csv")


num = list(n.array(list(range(0,105,5)))/100)
num1=[]
for i in num:
    data1["data1_pr_ran"] = (data1["y_pred_random_forest"]>=i).astype(int)

    tp=sum((data1["y_act"]==1) & (data1["data1_pr_ran"]==1))
    tn=sum((data1["y_act"]==0) & (data1["data1_pr_ran"]==0))
    fp=sum((data1["y_act"]==0) & (data1["data1_pr_ran"]==1))
    fn=sum((data1["y_act"]==1) & (data1["data1_pr_ran"]==0))

    tpr=tp/(tp+fn)
    fpr=fp/(fp+tn)

    num1.append([tpr,fpr])
    
graph=p.DataFrame(num1,columns=["x","y"])

from numpy import trapz
ds=trapz(graph.x,graph.y)
print(abs(round(ds)))

plot.scatter(graph.y,graph.x)
plot.show()


#character error

from nltk.metrics import edit_distance

letter1="this is a boy"
letter2="this is a girl"

print("character_error:" , edit_distance(letter1,letter2)/len(letter1))

#word error

word=letter1.split()
word1=letter2.split()

print("word_error:",edit_distance(word,word1)/len(word))

#prc

x_kaar=n.array([1,0,0,0,0,1])

y_pro=n.array([0.4,0.7,0.3,0.8,0.2,0.9])

print('prc rate:', metrics.average_precision_score(x_kaar,y_pro))

#mean absoulte error

value=0
len_val=len(data1)

for i,val in data1.iterrows():
    result = val["y_act"]-val["y_pred_random_forest"]
    value+=result

value=value/len_val

print("man absoulte value:",value)

#mean squre error 
to=0
for i,val in data1.iterrows():
    result = val["y_act"]-val["y_pred_random_forest"]
    result*=result
    to+=result

print("mean squre error:",to)