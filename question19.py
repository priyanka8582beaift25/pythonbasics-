# 19.Write a Python program to print a multiplication table of a given number.

number=int(input("Enter number:"))
for i in range (1,11) :
    table = number * i 
    print(number,"*",i,"=",table)