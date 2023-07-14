import base64

with open("story.txt","r") as f1:
    data=f1.read()

encode_val=base64.b64encode(data.encode("utf-16"))
print(encode_val)
print("encode successfully completed!!!!!!!!!!!!!!!!!!")

with open("aaa.txt","wb") as f2:
    f2.write(encode_val)
    
decode_val=base64.b64decode(encode_val).decode("utf-16","ignore")

# decode_val1=(decode_val.decode("utf-8","strict"))


with open("entoda.txt","w") as f3:
    f3.write((decode_val))


