number=int(input("enter the number: "))
original=number
mul=1
while number>0:
    dig=number%10
    mul=mul*dig
    number//=10
print(f"the product of  digit of {original} is {mul}")