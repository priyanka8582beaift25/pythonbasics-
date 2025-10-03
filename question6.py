# 6.Write a Python program to find the largest of three numbers.

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a>b and a>c :
    print(a, " is the largest among",a,",",b,",",c)
elif b>c : 
    print(b,"is the largest among",a,",",b,",",c)
else: 
    print(c,"is the largest among ",a,",",b,",",c)
