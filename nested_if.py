#greatest of three
number1=int(input("enter the number"))
number2=int(input("enter the number"))
number3=int(input("enter the number"))
if number1>number2:
          if number1>number3:
                 print(f"{number1 } is greatest")
          else:
              print(f"{number3} is greatest")
else:
    if number2>number3:
        print(f"{number2} is gratest")
    else:
        print(f"{number3} is greatest")
              

    