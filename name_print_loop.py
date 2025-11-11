#name prinnter this prints the name you enter for as many time you wanna print
name=input("Enter the name: ")
i=1
e=int(input("Enter how many times you wanna print"))
count=0
while i<=e:
 print (f"{i}.{name}")
 count+=1
 i+=1
print(f"here loop executed for {count} times")

 
 
 