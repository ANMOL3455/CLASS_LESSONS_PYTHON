#syntax
#1>> [expression for loop] 
#2>> [expression for loop condition]

#>>------ When to use condition and not using it

#example
l=[1,2,3,4,5,6,7]
print(l)
l1=[1,2,3,4,5,6,7]
print(l1)
l2=l1.copy()
print(l2)
l3=[x for x in l]
print(l3)
l4=[m for m in l if m%2==0]
print(l4)
l5=[m**2 for m in l]
print(l5)

#create a list having only element exactly divisible by 5 from 10-100
l0=[range(10,101)]

l9=[int(x) for x in range(10,101) if x%5==0]

l9=[x for x in range(10,101) if x%5==0]
print(l9)