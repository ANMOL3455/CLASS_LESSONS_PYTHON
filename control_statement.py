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