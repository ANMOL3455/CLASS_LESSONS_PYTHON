marks1=eval(input("enter the marks 1: "))
marks2=eval(input("enter the marks 2: "))
marks3=eval(input("enter the marks 3: "))
marks4=eval(input("enter the marks 4: "))
marks5=eval(input("enter the marks 5: "))
avg=(marks1+marks2+marks3+marks4+marks5)/5
if avg>80 and avg<100:
    print("he got distinction")
elif avg<80 and avg>=60:
    print("he got 1st division")
elif avg<60 and avg>=50:
    print("he got 2nd division")
elif avg<50 and avg>=40:
    print("he got 3rd division")
else:
    print("you are fail")
    
    
    
