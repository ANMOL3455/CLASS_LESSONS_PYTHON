#variable decleration
a=20
b=10

#Arithmetic Operators
#----------------------------
print("\nTHESE ARE ARTHEMATIC OPERATORS: ")
print(f"the addition is : {a+b}")
print(f"the substraction is: {a-b}")
print(f"the division is: {a/b}")
print(f"the product is : {a*b}")
print(f"the remainder is: {a%b}")
print(f"the floor division is: {a//b}")
print(f"the expo is :{a**b}")


#Comparision Operators
#------------------------------
#note the answers are
print("\nTHESE ARE COMPARISION OPERATORS: ")
print(f"{a} is greater than {b}: {a>b}")
print(f"{b} is greater than {a}: {b>a}")
print(f"{a}is equal to {b}: {a==b}")
print(f"{a} is not equal to {b}: {a!=b}")
print(f"{a} is greater or equal to {b}: {a>=b}")

#Logical Operators
#-----------------------------------
c=34
print("\nTHESE ARE LOGICAL OPERATORS: ")
print(f"{a} and {b} are greater than {c} = {a and b >c }")
print(f"{a} or {b} is smaller than {c} = {a or b <c }")
#using not
one=True
print(f"The opposite of true is : {not one }")

#Logical Operators in fundamentals
#-----------------------------------
print(10 and 20)
print(0 and 30)
print("hello" and "world")

print(10 or 30)
print(0 or 50)
print("sapkota" or "anmol")

#Bit wiae Operators
#-----------------------------------

#&==bitwise and
#|==bitwise or
#^==bitwise xor
#~==bitwise negation
#same as logical operator but does with bits of givrn operators
#first the number are converted into bits and only the logical operation are performed:
print(52 & 46)
print(5 | 6)
print(5 ^ 6)
#-------------------------------------
#>>==bitwise rightshift
#<<==bitwise leftshift
print(10 << 3)
print(52 >> 2)
print(~100)
print(~-100)

#Assignment operators
#-----------------------------------
a+=5
print(f"after a+=5 the value of a is {a}")
a-=5
print(f"after a=5 the value of a is {a}")
a/=34
print(f"after a/=5 the value of a is {a}")
#here data is also operated and stored in same variable after change

#Membership operators
#-----------------------------------
roll_no=[12,23,45,67,89,90,89]
print(f"is 30 in yhe list: {30 in roll_no}")
print(f"60 is not in list: {60 not in roll_no}")

#Identity Operstors
#--------------------------------------
#fundamental data
value_1=30
value_2=30
print(value_1 is value_2)
print(value_1==value_2)
#it is false as the operation works on address comparision as tehre are two objects formed with different address
ai=[12,23,45,67,89,90,89]
bi=[12,23,45,67,89,90,89]
print(ai is bi)
print(ai==bi)

#in is not it give T on different address and F on same address [memory address       ] 





