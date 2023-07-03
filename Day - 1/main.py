path_file = input("enter path:")
user_input= input("enter ur input")

try:
    with open(path_file,"w") as f1:
        f1.write(user_input)
    print("sucessfully Run")
   
except Exception as e:
    print("Error " + str(e))