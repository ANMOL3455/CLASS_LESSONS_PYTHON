number=int(input("Enter a number: "))
original=number
org=number
#calculating the  no of digits in the number goven
count=0
while number>0:
    dig=number%10
    count+=1
    number//=10  
cbs=0
while org>0:
    dig=org%10
    cbs=(dig**count)+cbs
    org//=10
if cbs==original:
    print("the number is armstrong")
else:
    print("not armstrong")
    