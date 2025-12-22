# this page will teach you to use reduce() function
#reduce cannot be used directly so for acessing reduce() first we should import functools
import functools as f
l=[1,2,3,4,5,6,7,8,9,10]
#syntax:
#variable = (function , collection_data_type)
m=f.reduce( lambda x,y : x+y , l)
print(f"the sum is: {m}")
