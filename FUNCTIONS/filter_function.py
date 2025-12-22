# it helps us filter the data according to our needs
#example >> filter all the even numbers in a list
def number_is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
    
numbers = [1,2,3,4,5,6,7,8,9,10,11]
even_numbers = list(filter(number_is_even,numbers))
print(f"numbers: {numbers}")
print(f"even_numbers: {even_numbers}")



def number_is_prime(n):
    i=2
    count=0
    while i <n:
     if n%i!=0:
         count+=1
         break
         i+=1
        
     if count==0:
        return True
     else:
        return False
    
numbers = [1,2,3,4,5,6,7,8,9,10,11]
prime_numbers = list(filter(number_is_prime,numbers))
print(f"numbers: {numbers}")
print(f"prime_numbers: {prime_numbers}")