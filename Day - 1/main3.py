import os

path_name = input("enter path name:")
file_name = input("enter file name:")

file1=open(file_name,"a")

for i in os.listdir(path_name):
    if i.endswith(".txt"):
        file2=open(path_name+'\\'+ i,'r')
        file1.write(file2.read() + '\n')
        file2.close()

print("Sucessfully append")

file1.close()