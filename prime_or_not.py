#prime or mot checker
number=int(input("Enter a number"))
i=2
count=0
while i<(number//2):
    if number%i==0:
      count+=1
      break
    i+=1
if count==0:
    print("the number is prime")
else:
    print("the number is composit")
    
    