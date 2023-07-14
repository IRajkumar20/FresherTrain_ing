from encodings.aliases import aliases

#encode and decode

# string="rajkumar"
# en=string.encode("ascii")

# print(en)

# print(en.decode("ascii"))

#encode and decode password

import base64


password="place@123₹fara"

encode_val=base64.b64encode(password.encode("utf-8",errors='strict'))

print(encode_val)

decode_val=base64.b64decode(encode_val).decode("utf-8",errors='strict')
print(decode_val)
