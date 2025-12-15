#with argument but no returntype:
def reverseee(given_number):
  original=given_number
  reverse=0
  while given_number>0:
   reminder=given_number%10
   reverse=reverse*10+reminder
   given_number=given_number//10
  print(f"the {original} number is {reverse}")

m=int(input("Enter the number: ")) 
reverseee(m)

#no argument  no returntype:
def reverseee():
  given_number=int(input("Enter the number: ")) 
  original=given_number
  reverse=0
  while given_number>0:
   reminder=given_number%10
   reverse=reverse*10+reminder
   given_number=given_number//10
  print(f"the {original} number is {reverse}")

reverseee()

#with argument and with returntype:
def reverseee(given_number):
  original=given_number
  reverse=0
  while given_number>0:
   reminder=given_number%10
   reverse=reverse*10+reminder
   given_number=given_number//10
  return reverse

m=int(input("Enter the number: ")) 
print(f"the reverse is: {reverseee(m)}")

#no argument and with returntype:
def reverseee():
  given_number=int(input("Enter the number: ")) 
  original=given_number
  reverse=0
  while given_number>0:
   reminder=given_number%10
   reverse=reverse*10+reminder
   given_number=given_number//10
  return reverse

print(f"the reverse is: {reverseee()}")


