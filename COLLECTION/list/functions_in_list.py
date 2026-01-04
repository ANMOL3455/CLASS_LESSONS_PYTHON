#useful function in list
#----------------------------------------------------------------------------------------------------#useful function in list

#1>> len()      >>counts the length of the list
#example:
list_1=[1,2,3,4,5,6,7,8,9,"anmol"]
print(f"The length is: {list_1}")

#2>> count()    >>counts the no of element you want to find
#example:
list_1=[1,4,3,4,5,6,7,4,9,"anmol"]
print(f"The count of 4 is: {list_1.count(4)}")

#3>> index()    >>find the index of the given element of the list 
#example:
list_1=[1,4,3,4,5,6,7,4,9,"anmol"]
print(f"The index of  anmol is: {list_1.index("anmol")}")

#----------------------------------------------------------------------------------------------------
#4>> append()   >>add the data in the list at last index
list_1.append("sapkota")
print(f"new list: {list_1}")

#----------------------------------------------------------------------------------------------------
#5>> insert()   >>insert the data in the given index
list_1.insert(4,9000)
print(f"new list: {list_1}")
#if i give the index that isnt present here the element will be added at last
list_1.insert(400,9000)
print(f"new list: {list_1}")

#----------------------------------------------------------------------------------------------------
#6>> extend()   >>extending the list
#the extending data should be given as collection type only either list,tuple or set
l=["ram","hari","kanxa"]
print(f"before extension: {l}")
l.extend([1,2,3])
print(f"after extension: {l}")
#string can be extended bit not the integer
l5=["ram","hari","kanxa"]
print(f"before extension: {l}")
l.extend("hari")
print(f"after extension: {l}")

dico={"anmol":"name","sap":"ls"}
l.extend(dico)
print(l) #in dictionary extension adds only keys
#----------------------------------------------------------------------------------------------------

#7>> remove()   >>to remove the specific data from the list
l.remove("ram")
print(l)
#----------------------------------------------------------------------------------------------------
#8>> pop()      >>to remove the last element
l.pop()
print(l)
#----------------------------------------------------------------------------------------------------
#9>> reverse()  >>reverse the list
print(f"before reverse: {l}")
l.reverse()
print(f"after reverse: {l}")
#----------------------------------------------------------------------------------------------------#useful function in list

#10>> sort()     >>sorts according to ascending and descending in list
marks=[12,34,56,73,23,45,56,65,34]
print(f"before sort: {marks}")
marks.sort() #ascendinf
print(f"before sort: {marks}")
marks.sort(reverse=True)
print(f"before sort: {marks}")
#----------------------------------------------------------------------------------------------------#useful function in list

#11>> clear()    >>clears the list
l.clear()
print(l)