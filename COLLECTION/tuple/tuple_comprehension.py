t1=(1,2,3,4,5,6,7,8)
print(type(t1))
t1=[x for x in t1 if x%2==0]
print(type(t1))
print(t1)

#does type conversion if use another identifier

#actually tuples cannot be compressed 


#summary:
#|----------------------------------------------|----------------------------------------------------------|
#|                 LIST                         |                  TUPLE                                   |
#|----------------------------------------------|----------------------------------------------------------|
#|                 mutable                      |immutable                                                 |
#|----------------------------------------------|----------------------------------------------------------|
#|                 comprehsion(supportive)      |comprehsion(unsupportive)                                 |
#|----------------------------------------------|----------------------------------------------------------|
#|                 change happens in existing   |if tried to change new objects will be created            |
#|                                              |with those changes occurs except indexing                 |
#|----------------------------------------------|----------------------------------------------------------|