#anything that is enclosed inside a single,double ir triple quotes.
#------------------------------
#>>>> PROPERTIES
#-----------------------------
#1 Insertion order is preserved i.e can do slicing and indexing.
#2 Duplication of data is allowed.
#3 IT doesnt support Mutability.


#------------------------------
#>>>> Ways of creation of string
#-----------------------------
#1>> Empty string
a=" "
a=str()
#2>> String with known element
greet="hello"
#3>>Dynamic asking with input()
name=input("Enter the name: ")
#4>>using eval
name=eval(input("Enter the name: "))
#5>>using str()
name=str(input("Enter the name: "))

#------------------------------
#>>>> Arthmetics opration in  string
#-----------------------------

#addition:
#both operands shoud be string
m,n="rai","maila"
print(f"{m+n}") #correct
print(f"{m*n}") #in correct

#multiplication:
#one of the operands should be integer
print(f"{m*n}") #in correct
a,b=1,"hari"
print(f"{a*b}") #in correct


#------------------------------
#>>>> Arthmetics opration in  string
#-----------------------------

#(==) and (<  /  >):
#both of the operands should be string
#For(==): to be true
#length of the string must be equal
#sequence of the string must be same
#case of the string must be same

#For(<  >): to be true
#based on the asciii value of a character or occurance


#------------------------------
#>>>> Transversing of a string
#-----------------------------
#it is about pring or reaching on every character of the string provided.
#can be read at >>>>>>>>  strings.py  <<<<<<


