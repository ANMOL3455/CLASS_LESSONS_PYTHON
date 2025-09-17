#here we have string datatype
#assignning a value toa variable
name="ramsaila"
#printing the string
print("my name is: ",name)
#indexing
#as the strings are stored in the form of characters and each have its own address and that particular
#address is called index
#lets see the example
print("the first letter is stored in the first place ad its address is",name[0]) #>>>> r
#NOTE-- indesing always starts with 0
#now lets see the slicing
#slicing means printing the particular slice or the sequecial data from a string
#the syntax is :: Variable_name[start:end-1:step]
#example:
last_4=name[4:9:1]
print("the last 4 letters of my name are: ",last_4)
#you can even do the negative indexing thta starts from the back ie: -1,-2,-3 etc
#example reversing the string with the help of reverse index slicing
reverse_name=name[-1:-9:-1]
print("the reversed name is",reverse_name)
#now you can create ur own logics and practice make sure to check out the quextions 😊

