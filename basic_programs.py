#simple programs related to arthemetic operators:
#1>>area of rectangle
print("For area of rectangle: ")
length_rectangle=eval(input("enter the length of rectangle: "))
bredth_rectangle=eval(input("enter the breadth of rectangle: "))
print(f"The area of rectangle is: {length_rectangle*bredth_rectangle}")


print("\n")
#2>>area of square
print("For area of Square: ")
length_square=eval(input("enter the length: "))
print(f"the area of square is: {length_square**2}")


print("\n")
#3>>area of circle
print("For area of Circle: ")
radius=eval(input("enter the radius of the circle: "))
print(f"The area of the circle with radius {radius} is : {3.14*radius}")



print("\n")
#4>>volume of cuboid
print("For volume of cuboid:  ")
length_cuboid=eval(input("enter the length of cuboid: "))
bredth_cuboid=eval(input("enter the breadth of cuboid: "))
height_cuboid=eval(input("enter the height of the cuboid: "))
print(f"the volume of the rectangle is: {length_cuboid*bredth_cuboid*height_cuboid}")


print("\n")
#5>>volume of cube
print("For volume of cube: ")
length_cube=eval(input("enter the length of cube: "))
print(f"The volume of cube is: {length_cube**3}")


print("\n")
#6>>perimetre of Square
print("For perimetre of square: ")
length_square=eval(input("enter the length: "))
print(f"The perimeter of square is: {4*length_square}")


print("\n")
#7>>Simple Intrest
print("For simple intrest: ")
time=int(input("enter the time: "))
principle=int(input("enter the principle: "))
rate=int(input("enter the rate: "))
print(f"the si is: {(principle*time*rate)/100}")


print("\n")
#8>>Velocity calculator
print("For velocity of a vechile: ")
distance_travelled=eval(input("enter the total distance travelled in metre: "))
time_taken=eval(input("enter the time taken to travel the distance in second: "))
print(f"the velocity of the vechile is: {distance_travelled/time_taken}")


print("\n")
#9>>profit loss calculator
print("Profit loss Calculator: ")
selling_price=eval(input("Enter the selling price of the good in RS: "))
Cost_price=eval(input("Enter the Cost price of the good in RS: "))
calculate=Cost_price-selling_price
if(Cost_price>selling_price):
    print(f"you had an loss of: RS {calculate}")
else:
    print(f"You had an profit of : RS {-1*calculate}")


print("\n")
#10>>time calculator
print("time converter HR to minutes and seconds: ")
time_given=eval(input("enter the time in hour: "))
print(f"{time_given} HOUR is equal to {time_given*60} minutes")
print(f"{time_given} HOUR is equal to {time_given*60*60} seconds")
