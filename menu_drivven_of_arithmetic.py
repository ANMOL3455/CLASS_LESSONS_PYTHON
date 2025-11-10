print("this is a menu drivven program : ")
print(" 1>> Addition\n 2>>Subtraction\n 3>>Division \n 4>>Product")
choice=int(input("enter your choice: "))
match choice:
    case 1:
        number_1=eval(input("enter the first number: "))
        number_2=eval(input("enter the second number: "))
        print(f"The addition is {number_1+number_2}")
    case 2:
        number_1=eval(input("enter the first number: "))
        number_2=eval(input("enter the second number: "))
        print(f"The substration is {number_1-number_2}")
    case 3:
        number_1=eval(input("enter the first number: "))
        number_2=eval(input("enter the second number: "))
        if number_2==0:
            print("the nunomenator cannot be 0")
        else:
         print(f"The quotent is {number_1/number_2}")
    case 4:
        number_1=eval(input("enter the first number: "))
        number_2=eval(input("enter the second number: "))
        print(f"The quotent is {number_1*number_2}")
    case _:
        print(f"{choice} is not in the menu: ") 