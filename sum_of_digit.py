number=int(input("enter the number: "))
original=number
sum=0
while number>0:
    dig=number%10
    sum=sum+dig
    number//=10
print(f"the addition of  digit of {original} is {sum}")

