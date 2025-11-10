number=int(input("enter the week number: "))
match number:
 case 1:
    print("the day is Sunday")
 case 2:
    print("the day is monday")
 case 3:
    print("the day is tuesday")
 case 4:
    print("the day is wednesday")
 case 5:
    print("the day is thrusday")
 case 6:
    print("the day is friday")
 case 7:
    print("the day is saturday")
 case _:
    print(f"enter the correct number {number} not in week")
    
