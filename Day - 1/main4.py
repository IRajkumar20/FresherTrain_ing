path_name = input("Enter path name:")
try:
    with open(path_name,'r') as f1:
        lines=f1.readlines()
        print(lines)
    print("sucessfull read lines")

except Exception as e:
    print("ERROR!!! " + str(e))

