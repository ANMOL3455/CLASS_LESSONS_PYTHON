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
