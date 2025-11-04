#takes data in seperated datas on heir specific variables
#using spit helps in seperating the data accPording to the variable: 
name1,name2,name3,name4=input("enter te name of students saperated by space: ").split()
print(name1)

#using list
names=input("enter te name of students saperated by space: ").split()
for name in names:
    print(f"name is {name}")
    
#taking multiple input and finding its average;
num1,num2,num3,num4,num5=[int(number) for number in input("enter the five numbers seperated by space: ").split()]
print(f"the average is {(num1+num2+num3+num4+num5)/5}")
