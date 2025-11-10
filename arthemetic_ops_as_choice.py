number1=int(input("enter the number: "))
number2=int(input("enter the number: "))
choice=input("enter yiut choice: [+,-,*,/,%]")
if choice=="+":
    print(f"the addition of {number1} and {number2} is: {number1+number2}")
elif choice=="-":
    print(f"the difference of {number1} and {number2} is: {number1-number2}")
elif choice=="*":
    print(f"the product of {number1} and {number2} is: {number1*number2}")
elif choice=="/":
    print(f"the quotent of {number1} and {number2} is: {number1/number2}")
elif choice=="%":
    print(f"the reminder of {number1} and {number2} is: {number1%number2}")
else:
    print(f"invalid choice {choice}")

