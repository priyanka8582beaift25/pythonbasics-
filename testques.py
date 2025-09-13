# 1.Write a python program to take an integer, float, and string input from the user and print them using f-string 

# a=int(input("Enter integer:"))
# b=float(input("Enter float:"))
# c=str(input("Enter a string:"))
# print(f"{a} is an integer")
# print(f"{b} is float")
# print(f"{c} is a string ")


# 2.Write a program to check the type of variable : integer, float, list, tuple, string, dictionary

# var = 23.45
# if type(var) == int:
#     print("Type: Integer")
# elif type(var) == float:
#     print("Type: Float")
# elif type(var) == list:
#     print("Type: List")
# elif type(var) == tuple:
#     print("Type: Tuple")
# elif type(var) == str:
#     print("Type: String")
# elif type(var) == dict:
#     print("Type: Dictionary")
# else:
#     print("Type: Unknown")


# 3.Write a program that takes two numbers as input and prints their sum, difference, product, and division 

# num1 = int(input("enter num1:"))
# num2 = int(input("enter num2:"))
# sum = num1 +num2 
# diff = num1 - num2 
# product = num1*num2 
# division = num1/num2 
# print ("The sum of numbers is :",sum)
# print("The diff of numbers is : ",diff)
# print("The product of numbers is :",product)
# print("The division of numbers is :",division)


# 4.Write a program that converts Celsius to Fahrenheit.

# celsius =int(input("Enter the value ="))
# fahrenheit= (celsius*9/5)+32 
# print(celsius,"°C =",fahrenheit,"°F")


# 5.Write a program that takes your name and age as input and prints: 'My name is X and I am Y years old

# name = input("Enter your name :")
# age = int(input("Enter your age :"))
# print(f"My name is {name} and I am {age} years old.")


# 6.Write a program to swap two variables using input from the user.

# a = int(input("Enter any number,a :"))
# b = int(input("Enter any number,b :"))
# print("Before swapping : a,b =",a,",",b)
# a = a+b
# b = a-b 
# a = a-b
# print("After swapping :a,b=",a,",",b)


# 8.Write a program to perform all arithmetic operations on two numbers

# a=int(input("Enter 1st Number :"))
# b=int(input("Enter 2nd Number :"))
# sum=a+b
# print("Sum of a and b is : ",sum)
# if a>b :
#     print("Difference is :", a-b)
# else :
#     print("Difference is :",b-a )
# product= a*b
# print("Product of a and b is :",product)
# division= a/b
# print("Division of a and b is :",division)
# modulus=a%b
# print("Modulus of a and b is :",modulus)


# 9.Write a program to check whether two numbers are equal using comparison operators.

# a=int(input("Enter 1st Number :"))
# b=int(input("Enter 2nd Number :"))
# if a==b :
#     print("Numbers are equal")
# else :
#     print("Numbers are not equal ")


# 11.Write a program to check whether a number lies between 10 and 50 using logical operators.

# a=int(input("Enter Number :"))
# if a>10 and a<50 :
#     print(a,"lies between 10 and 50")
# else :
#     print(a,"does not lie between 10 and 50")


# 12.Write a program to check membership of an element in a list using 'in' and 'not in'.

# list=['mango','guava','plum','peach','grapes','litchi']
# if 'pink' in list :
#     print ("Is a member ")
# else :
#     print("Is not a member ")


# 14.Write a program to check whether a number is positive, negative, or zero.

# num=float(input("Enter number:"))
# if num >0 :
#     print(num,"is positive")
# elif num <0 :
#     print(num,"is negative")
# else :
#     print(num,"is zero")


# 15.Write a program to check whether a number is even or odd using if-else.

# a = int(input("Enter the number:"))
# if a<0 :
#     print("Enter a positive number") 
# elif a %2 == 0 :
#     print(a," is Even")
# else : 
#     print(a,"is Odd")


# 16.Write a program to find the largest of three numbers using nested if-else.

# a = float(input("Enter the number:"))
# b = float(input("Enter the number:"))
# c = float(input("Enter the number:"))
# if a > b:
#     if a > c:
#         print("The largest number is:", a)
#     else:
#         print("The largest number is:", c)
# else:
#     if b > c:
#         print("The largest number is:", b)
#     else:
#         print("The largest number is:", c)


# 17.Write a program to print all numbers from 1 to 20 using a for loop.

# for i in range (1,21):
#     print(i) 


# 18.Write a program to print the multiplication table of a given number using a while loop.

# number=int(input("Enter the number:"))
# i=1
# while i <=10 :
#     table = number * i 
#     print(number,"*",i,"=",table)
#     i=i+1


# 20.Write a program to check whether a number is prime using a while-else.

# num = int(input("Enter a number: "))
# # Prime numbers are greater than 1
# if num <= 1:
#     print(num, "is not a prime number.")
# else:
#     i = 2
#     while i < num:
#         if num % i == 0:
#             print(num, "is not a prime number.")
#             break
#         i += 1
#     else:
#         print(num, "is a prime number.")


# 21. Write a program that prints numbers from 1 to 10 but skips 5 using continue.

# for i in range(1,11):
#     if i==5 :
#         continue
#     print(i)


# 22.Write a program that prints numbers from 1 to 10 but stops when it reaches 7 using break

# for i in range (1,11):
#     if i<=7:
#         print(i)
#     else:
#         break 


#23. Write a program that prints 'Hello' five times but does nothing when the loop counter is 3 (use pass).

# for i in range (1,6): 
#     if i==3:
#         pass
#     else:
#         print(i,"Hello")


# 25. Write a program to generate squares of numbers using a for loop with an iterator

# for i in range (1,11) :
#     print("Square of",i,"is",i**2)


# 7. Write a program to check whether a variable is mutable or immutable in Python (by attempting modification).
# 10. Write a program to demonstrate bitwise operators (&, |, ^, <<, >>) on two numbers
# 13. Write a program to compare two objects using 'is' and 'is not'.
# 19. Write a program to search an element in a list using for-else.
# 24. Write a program to create an iterator for a list and print all elements using next().