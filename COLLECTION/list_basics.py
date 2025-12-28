


#|||||                         ||||||||||||||||||||              ||||||||||||||||||||              ||||||||||||||||||||
#|||||                         ||||||||||||||||||||              ||||||||||||||||||||              ||||||||||||||||||||
#|||||                                ||||||                     |||||                                     ||||
#|||||                                ||||||                     |||||                                     ||||
#|||||                                ||||||                     ||||||||||||||||||||                      ||||                  
#|||||                                ||||||                     ||||||||||||||||||||                      |||| 
#|||||                                ||||||                                    |||||                      ||||
#|||||                                ||||||                                    |||||                      ||||               
#|||||||||||||||||||||         ||||||||||||||||||||              ||||||||||||||||||||                      ||||
#|||||||||||||||||||||         ||||||||||||||||||||              ||||||||||||||||||||                      ||||
#                                                                



#>>------------------------------------------
# properties
#>>------------------------------------------

# 1>> identified by [ ]
# 2>> indexing and slicing are possible
s=[1,4,6,8]
print(s[0])  #as 1 is in first position and comes in first one so insertion order is preserved
     
# 3>> supports homo and hetro datas
#hetro >> different types of data
#homo >> same type of datad

# 4>> supports duplicacy
#example
list0=[10,10,10]

# 5>> supports mutability
list0=[10,10,10]
print(list0)

list0[2]=34
print(list0)


#>>------------------------------------------
# *ways to create a list:
#>>------------------------------------------

#     1>> empty list can be created as >> l=[]
#example
empty_list=[]

#     2>> list with known element can be created as >> l=[1,2,3,45]
#example
known_list=[12,"rt",34,67]

#   3>> dynamic list using eval
#example
list_=eval(input("Enter a list: "))

#   4>> list with split( ) function
#example
s="ktm is nepal's capital"
list_splited=s.split()

#   5>> List with list() function
s="rameykaila"
l=list(s)
