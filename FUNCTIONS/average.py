#this function takes the value from the average function
def printing(avg):
    print(f"the average is: {avg}")
    
#this function takes the value from the add function
def average(sum):
    avg=sum/3
    printing(avg)
    

def add(a,b,c):
    sum=a+b+c
    average(sum)
    
    
    
add(12,34,56)