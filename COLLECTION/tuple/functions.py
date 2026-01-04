#>---------------------------------------------------
#1>> len()
#2>> count()
#3>> index()
#4>> sorted()
#5>> min()
#6>> max()
#>---------------------------------------------------
#example :

#1>> len() >> used to calculate the length of the tuple
tp=1,5,3,4,7,5,4,3,5,6,78,8
print(f"The length is: {len(tp)}")

#2>> count() >> used to calculate the occurance of element in tuple
print(f"the count of 5 is {tp.count(5)}")

#3>> index() >> used to find the index of element in tuple
print(f"the index of first '7' is {tp.index(7)}")

#4>> sorted() >> used to sort the element in tuple
print(f"the sorted data is: {tuple(sorted(tp))}")

#5>> min() >> used to find the minimum element in tuple
print(f"the smallest data is {min(tp)}")

#6>> max() >> used to find the maximum element in tuple
print(f"the largest data is {max(tp)}")


