#to find weather the given year is leap year or not:
year=int(input("Enter the year you wanna check: "))
if (year%4==0 and year%100!=0) or year % 400==0:
    print(f"the given year {year} is leap year")
else:
    print(f"the given year {year} is not leap year")


