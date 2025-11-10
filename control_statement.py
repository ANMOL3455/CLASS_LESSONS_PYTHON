#as we know that the code running is controlled by PVm but by using contro statements we can
#control the code running process as per te programmer
#there are three types of control statements theyare : 
#1>> selection based programming

#a> if ststement:
#SYNTAX:
#if <condition>
    #statement 1
    #statement 2
#else:
    #statement 1
    #statement 2

#example: 

print("you can only use the program if the code is >>>>>   445   <<<<")
code=int(input("enter the code: "))
if code == 445:
    print(":: completed you entered ::")
else:
    print(":: Error code ::")
    
#2 ladder if
#it includes if elif and else as a out statement
#example
#this is a program that reveals the day with the help of day name
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
    
