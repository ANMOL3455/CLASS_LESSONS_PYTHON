import sys
#the above module is used for the CLA

#>>-----------------------------------
#INPUT statements
#>>-----------------------------------
#1.Using input()  >> it is a pre defined function 
#example
number_1=int(input("enter the first number: "))
number_2=int(input("enter the second number: "))
print("The sum of numbers is : ",number_1+number_2)
print("The product of the numbers is: ",number_1*number_2)

#2.Using eval with input() >> helps in auto evaluation of input
data_1=eval(input("enter the number"))
data_2=eval(input("enter the number"))
print(f"the datas are : {data_1} and {data_2}")

#3.Command line argument
#in command line>> ---- python input output statement.py 10 20 30 
print(sys.argv)
#the output seems ["input output statement.py","10 20 30"]








#>>-----------------------------------
#OUTPUT statements
#>>-----------------------------------
#1.Message Printing
print("college")
print("lbef")
print("kathmandu")


#2 Value Printing
a=10
b=20
print(a)

#3 message and value printing
print("the value of a is: ",a)


#4 Print with end attribute
print("my name" , end=" ")
print("is ramji" , end=" ")
print("bhandari" , end=" ")
  
  
    #what if i dont use the end then the thing i print will go on new line

#5 Printing with sep attribute
a,b,c,d=10,20,30,40
print(a,b,c,d)
#default value of sep is " ";
  
  #using sep
print(a,b,c,d, sap=',') #here comma is seperation value

#6 Printing with format string
name="rai maila"
subject="computer"
age=20
print("name is %s subject is %s and age is %d" % (name,subject,age))

#7Printing with format modifier
pie=22/7
#without modifier
print(pie)
#with format modifier
print("%.2f" %(pie))

#8 Printing with format function
#short and simple
print(f"my name is {name} and i am studying {subject} and i am {age} years old")


#long one
print("name is {} subject is {}".format(name,subject))

#with index
print("name is {1} subject is {2}".format(name,subject))

#9 with format string
print(f"my name is {name} and i am studying {subject} and i am {age} years old")


