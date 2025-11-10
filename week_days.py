number=int(input("enter the week number: "))
if number==1:
    print("the day is Sunday")
elif number==2:
    print("the day is monday")
elif number==3:
    print("the day is tuesday")
elif number==4:
    print("the day is wednesday")
elif number==5:
    print("the day is thrusday")
elif number==6:
    print("the day is friday")
elif number==7:
    print("the day is saturday")
elif number<0:
  print(f"enter the correct number negative number not in week")  
else:
    print(f"enter the correct number {number} not in week")
    
