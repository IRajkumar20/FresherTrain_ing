# from sklearn import metrics
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import precision_score_score
# from sklearn.model_selection import train_test_split

import pandas as p
import numpy as n

data1=p.read_csv("data.csv")

data1["data1_pr_ran"] = (data1["y_pred_random_forest"]>=0.5).astype(int)
data1["data1_pr_loc"] = (data1["y_pred_logistic"]>=0.5).astype(int)

def computed(acc,y_pr):

    tp=sum((acc==1) & (y_pr==1))
    tn=sum((acc==0) & (y_pr==0))
    fp=sum((acc==0) & (y_pr==1))
    fn=sum((acc==1) & (y_pr==0))

    return tp,tn,fp,fn

tp,tn,fp,fn=computed(data1["y_act"],data1["data1_pr_loc"])

print(tn,tp,fp,fn)

#accuracy

def accurancy(tn,tp,fp,fn):
    accurancy_result=((tp+tn)*100)/float(tp+tn+fp+fn)
    print("accuracy:" + str(accurancy_result))

accurancy(tn,tp,fp,fn)

#precision

precision_result=(tp)*100/float(tp+fp)
print("precision_rate:" + str(precision_result))

#recall

recall_result=((tp)*100)/float(tp+fn)
print("recall_rate:" + str(recall_result))

#f1_score

precision=precision_result/100
recall=recall_result/100
f1_score_result= (2*precision*recall)/(precision+recall)
print("f1_score_rate:" + str(f1_score_result))


from nltk.translate.bleu_score import sentence_bleu
reference = [['this', 'is', 'a', 'test'], ['this', 'is' 'test']]
candidate = ['this', 'is', 'a', 'test']
score = sentence_bleu(reference, candidate)
print("Bleu_rate:",score)


