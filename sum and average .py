#this includes command line argument so give the input in command and only run the program:
import sys 
sum=0
for data in sys.argv[1:]:
    sum+=int(data)
print(f"the sum is: {sum}")
print(f"the average is {sum/5}")



    