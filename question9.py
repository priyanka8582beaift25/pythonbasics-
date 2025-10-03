# 9.Write a Python program to calculate grade of a student based on mark (if-elif ladder).

marks = float(input("enter the marks:"))
if marks>100:
    print("Invalid")
elif marks<0:
    print("Invalid") 
elif marks>=90 :
    print("Grade is A+")
elif marks>=75 :
    print("grade is A")
elif marks>=60 :
    print("Grade is B")
elif marks>=40 :
    print("Grade is C ")
else :
    print("Fail")