
#LIST

listo=[1,2,3,4,5]
print(listo)
print(f"the datatype is: {type(listo)}")
#counting the no of elements in the list
count=0
for number in listo:
    if number!=None:
        count+=1
#printing the  elements in the list
for number in listo:
     print(number)
print(f"the no of elements is: {count}")

#tuple

tupleo=(1,2,3,4,5)
print(tupleo)
print(f"the datatype is: {type(tupleo)}")
#counting the no of elements in the list
count=0
for number in tupleo:
    if number!=None:
        count+=1
#printing the  elements in the list
for number in tupleo:
     print(number)
print(f"the no of elements is: {count}")

#SET

seto={1,2,3,4,5,6,7}
print(set)
print(f"the datatype is: {type(set)}")
for number in seto:
    print(number)
count=1
for number in seto:
    if number!=None:
        count+=1
print(f"there are {count} set elements")
        
#dictionary
dicto={
    "name":"anmol",
    "class":13,
    "roll":23
}
for k,v in dicto.items():
    print(k,v) 
    
#range
print(f"the odd numbers are: ")
for i in range(1,50,2):
    print(i)



