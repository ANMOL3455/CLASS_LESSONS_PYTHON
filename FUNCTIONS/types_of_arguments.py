#Formal Arguments
def f1(a):
    print(f"hello i am a {a} developer")

f1("pro")

#here [ PRO ] is Formal parameter as it is defined during function defination


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#-------------------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#Actual Arguments
def f1(a):
    print(f"hello i am a {a} developer")

f1("pro")

#here [ a ] is actual parameter as it is defined during function defination

#----------------------------------------------------------------------------------
#OREDER OF SUBDIVISION:
#>>> Positional argument
#>>> Keyword argument
#>> Default argument
#>> Variable length argument
#>> should come after in order
#----------------------------------------------------------------------------------

#Sub division:
#1 >>> Positional argument
def add(a,b,c):
    sum=a+b+c
    print("the sum is: ",sum)
    
add(12,34,56)

#here 12 goes to a , 34 to b and so on

#2>>Keyword argument
def add(a,b,c):
    print(a,b,c)
    sum=a+b+c
    print("the sum is: ",sum)
    
add(c=12,b=34,a=56)

#here 12 goes to c , 34 to b and 56 to a
#test cases
#make sure no variable gets double value
#if you pass positional and keyword argument then keyword should be after positional


#3>>default argument
#has an fixed values of the argument
def add(a=10,b=11,c=12):
    print(a,b,c)
    sum=a+b+c
    print("the sum is: ",sum)
    
add()

# OR
def add(a,b=11,c=12):
    print(a,b,c)
    sum=a+b+c
    print("the sum is: ",sum)
    
add(a=30)

#OR
def add(a,b=11,c=12):
    print(a,b,c)
    sum=a+b+c
    print("the sum is: ",sum)
    
add(100,100,89)
#make sure default comes after nondefault
#here the new value of argument overwrites the default one

#3>>variable length argument
def add(*a):
    sum=0
    for number in a:
     sum+=number
    print("the sum is: ",sum)
    
add(1000,100,89)

#the above add function have argument " a "
#the argument gets the value of all the formal argument and keeps it as collection and it is tuple
 #next form of vvariable length argument: 
def add(**a):
    sum=0
    for value in a.values():
     sum+=value
    print("the sum is: ",sum)
    
add(an=1,bn=100,cn=89)
#the above add function have argument " a "
#the argument gets the value of all the formal argument and keeps it as collection and it is dictionary