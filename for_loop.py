#easy than  while loop
#>>>>>>>>>>>>SYNTAX
#for increment object {{{{ condition }}}} :
  #<<<   STATEMENT    >>>>
#example:
c=0
x=int(input("enter the starting: "))
y=int(input("enter the limit: "))
for i in range(x,y):
    if i%2==0:
        print(i)
        c+=1
print(f"there are {c} even number between 1  to 100")
