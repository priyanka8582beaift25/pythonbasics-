# 16.Write a Python program to print Fibonacci series up to n terms 

n=int(input("Enter no of terms:"))

a=0
b=1 
print("Fibonacci series:")
for i in range (n):
    print(a)
    a,b=b,a+b 