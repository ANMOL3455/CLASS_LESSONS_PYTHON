#wap to count and print  total no of leapyear of 21st centuary
year_i=2000
year_e=2100
c=0
while year_i<=2100:
     if (year_i%4==0 and year_i%100!=100) or year_i%400==0:
         print(year_i)
         c+=1
     year_i=year_i+1
print(c)
    
    
#wap to find multiplication tabele of given number
number=int(input("enter the number you wanna find the table of: "))
i=1
while i<=10:
    print(f" {number} x {i} = {i*number}") 
    i+=1
    
#wap to find the factorial of given number
number=int(input("Enter a number: "))
s=number
fact=1
while number>=1:
    fact=fact*number
    number=number-1
print(f"The factorial of {s} is {fact}")