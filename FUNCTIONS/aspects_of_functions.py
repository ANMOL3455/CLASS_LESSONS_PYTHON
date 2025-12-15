#Function with argument and without return type:
def f1(a):
    print(f"hello i am a {a} developer")

f1("pro")

#Function without argument and without return type:
def f2():
    type="pro"
    print(f"hello i am a {type} developer")

f2()

#Function with argument and with return type:
def f3(a):
    return a

print(f"I am a {f3("pro")} Developer")

#Function without argument and with return type:
def f4():
    type="pro"
    return type

print(f"I am a {f4()} Developer")