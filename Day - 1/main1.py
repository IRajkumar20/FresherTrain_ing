path_name=input("enter path name:")
# user_input=input("enter ur input:")

try:
    with open(path_name, "r") as file1:
        print(file1.read())
    print("sucessfully run")
except Exception as e:
    print("Error " + str(e))