#checking  the number if palindrome:
given_number=int(input("enter the number: "))
original=given_number
reverse=0
while given_number>0:
 reminder=given_number%10
 reverse=reverse*10+reminder
 given_number=given_number//10
if original==reverse:
    print("The number is palindrrome")
else:
    print("the number is not palindrome")


