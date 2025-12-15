khabar="  hari maila ko budi  "
#1>> len()
print(f"The length of the string is: {len(khabar)}")

#2>> strip()
print(f"The data after right and left spaces removed: {khabar.strip()}")

#3>> lstrip()
print(f"The data after  left spaces removed: {khabar.lstrip()}")

#4>> rstrip()
print(f"The data after right spaces removed: {khabar.rstrip()}")

#5>> find()
print(f"The index of o in the above string is: {khabar.find('o')}")

#6>> rfind()
print(f"The index of o in the above string is: {khabar.rfind('o')}")

#7 >> giving the range to find
print(f"The index of o in the above string is: {khabar.find(khabar.find('bud'),khabar.rfind('bud'),len(khabar))}")
