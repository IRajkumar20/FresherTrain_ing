import base64

with open("chinese.txt","rb") as f1:
    data=f1.read()

print(data)

encode_val=(data.decode("utf-8","ignore"))

print(encode_val)
print("encode successfully completed!!!!!!!!!!!!!!!!!!")

data1=encode_val

# print(data1)

# with open("output.txt","w",encoding="utf-8") as f2:
#     f2.write(data1)
    
