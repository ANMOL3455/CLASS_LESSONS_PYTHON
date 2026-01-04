#>---------------------------------------------------
#properties\
#>---------------------------------------------------
#1>> identified by ()
#2>> insertion order is preserved it means we can apply indexing and slicing
#3>> supports homo and hetro data
#4>> supports element duplicacy
#5>> Immutable in nature
#>---------------------------------------------------
#ways to create tuple:
#>---------------------------------------------------

#1>> Empty tuple
t=()
t1=tuple()

#2>> tuple with known element
Sub_marks=(10,10,20,30,40)

#3>> dynamic tuple using eval
f=eval(input("Enter a tuple: "))

#doesn't use split()

#4>> using tuple function
list1=[10,20,30,40,50]
tpp=tuple(list1)
