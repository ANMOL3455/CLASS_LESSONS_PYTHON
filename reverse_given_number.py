#reversing the number:
given_number=int(input("enter the number: "))
original=given_number
reverse=0
while given_number>0:
 reminder=given_number%10
 reverse=reverse*10+reminder
 given_number=given_number//10
print(f"the {original} number is {reverse}")

