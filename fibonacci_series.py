#WAP to print the fibonaccic series of the given element
limit=int(input("Eneter the limit number: "))
a=0
b=1
i=3
if limit>1:
 print(a,b)
 while i<=limit:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
else:
    print("enter the limit>1")   