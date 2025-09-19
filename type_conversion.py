# =============================
# Type Conversion in Python
# =============================
# Built-in conversion functions:
# int(), float(), complex(), str(), bool()
# Let's understand them one by one with examples and error cases.

# ------------------------------------
# 1. int()  -> converts to integer type
# ------------------------------------
# Works on: float (decimal is truncated), bool (True=1, False=0)
# Does NOT work on: string with non-numeric data, complex numbers

name = "thalmukhey"
weight = 23.4
mathe = 2+6j
truth = True

print("int of weight:", int(weight))    # 23  (decimal part is dropped)
print("int of truth:", int(truth))      # 1

# Error cases
# print(int(name))    # ERROR: invalid literal for int()
# print(int(mathe))   # ERROR: can't convert complex to int


# ------------------------------------
# 2. float()  -> converts to floating-point type
# ------------------------------------
# Works on: int, bool, numeric strings
# Does NOT work on: non-numeric strings, complex numbers

age = 20
truth = False
num_str = "56"

print("float of age:", float(age))      # 20.0
print("float of truth:", float(truth))  # 0.0
print("float of num_str:", float(num_str))  # 56.0

# Error cases
# print(float(name))   # ERROR: could not convert string to float
# print(float(mathe))  # ERROR: can't convert complex to float


# ------------------------------------
# 3. complex()  -> converts to complex number
# ------------------------------------
# Works on: int, float, bool, numeric strings
# Syntax: complex(real, imag) or complex(value)

num = 5
pi = 3.14
truth = True
num_str = "8"

print("complex of num:", complex(num))         # (5+0j)
print("complex of pi:", complex(pi))           # (3.14+0j)
print("complex of truth:", complex(truth))     # (1+0j)
print("complex of num_str:", complex(num_str)) # (8+0j)
print("complex with 2 args:", complex(3, 4))   # (3+4j)

# Error cases
# print(complex(name))   # ERROR: can't convert non-numeric string


# ------------------------------------
# 4. str()  -> converts to string type
# ------------------------------------
# Works on everything (safe conversion)

print("str of num:", str(num))       # "5"
print("str of pi:", str(pi))         # "3.14"
print("str of mathe:", str(mathe))   # "(2+6j)"
print("str of truth:", str(truth))   # "True"
print("str of name:", str(name))     # "anmol"
# no error case for str()

