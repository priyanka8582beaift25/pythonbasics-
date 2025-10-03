# 14.Write a Python program to calculate factorial of a number using while loop.

n=int(input("Enter number:"))
fact,i=1,1
while i<=n:
    fact*=i
    i+=1
print("Factorial is :",fact)