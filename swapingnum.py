# Program to swap two numbers without using a third variable (using arithmetic operators)

a = int(input("Enter any number,a :"))
b = int(input("Enter any number,b :"))
a = a+b
b = a-b 
a = a-b
print("After swapping :a,b=",a,",",b)

