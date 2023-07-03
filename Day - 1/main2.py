path_name=input("enter path name:")
user_input=input("enter ur msg:")
try:
    with open(path_name,"a") as f2:
        f2.write("\n"+user_input)
except Exception as e:
    print("error " + str(e) )