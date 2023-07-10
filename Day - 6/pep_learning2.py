class MyClass:

    def find_largest_number(): #function declare

        #get input from user
        first_number=int(input("Enter a first number:")) 
        second_number=int(input("Enter a second number:"))
        third_number=int(input("Enter a third number:"))
        
        #use condition
        if (first_number>second_number and
            first_number>third_number ):
            print(str(first_number) + " is a largest number!")
        
        elif (second_number>first_number and
            second_number>third_number):
            print(str(second_number) + " is a largest number!")

        else:
            print(str(third_number) + " is a largest number!")

    find_largest_number() #fuction call