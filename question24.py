# 24.Write a Python program to print Floyd's triangle.

n=int(input("Enter Number:"))
a=1
b=1
for i in range (1,n+1):
    for j in range(i):
        print(a,end=" ")
        a,b=a+1,b+2
        print()