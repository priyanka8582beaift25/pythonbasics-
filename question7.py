# 7.Write a Python program to check whether a given year is a leap year.

year=int(input("Enter Year:"))
if year %4 ==0 :
    print("Given year,",year,",is a leap year")
else :
    print("Given year,",year,",is not a leap year ")