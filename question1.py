# 1.write a Python program to swap two numbers  without using a third variable 

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print("Before swapping:a,b=",a,",",b)
a=a+b
b=a-b
a=a-b
print("After swapping:a,b=",a,",",b)