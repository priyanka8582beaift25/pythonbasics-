# 1.write a Python program to swap two numbers  without using a third variable 

# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# print("Before swapping:a,b=",a,",",b)
# a=a+b
# b=a-b
# a=a-b
# print("After swapping:a,b=",a,",",b)

#OUTPUT
# Enter 1st number:34
# Enter 2nd number:56
# Before swapping:a,b= 34 , 56
# After swapping:a,b= 56 , 34


# 2.Write a Python program to check whether a given number is even or odd

# num=int(input("Enter number:"))
# if num % 2==0 :
#     print(num,"is Even ")
# else :
#     print(num, "is Odd")

#OUTPUT
# Enter number:45
# 45 is Odd
# Enter number:54
# 54 is Even 


# 3.Write a Python program to calculate the area and circumference of a circle given the radius

# radius=float(input("Enter radius : "))
# area= 3.14 *(radius**2)
# circumference=2*3.14*radius 
# print("Area of circle is",area)
# print("Circumference of circle is",circumference)

#OUTPUT
# Enter radius : 4
# Area of circle is 50.24
# Circumference of circle is 25.12


# 4.Write a Python program to accept a string and put it in reverse order 

# def reverse_string(string):
#     return string[::-1]
# string=input("Enter String:")
# reverse=reverse_string(string)
# print("Reverse of the string entered is :",reverse)

#OUTPUT
# Enter String:Priyanka
# Reverse of the string entered is : aknayirP


# 5.Write a Python program to accept two integers and perform addition, subtraction, multiplication, division, and modulus

# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# print("Sum=",a+b)
# print("Subtraction=",a-b)
# print("Multiplication=",a*b)
# print("Division=",a/b)
# print("Modulus=",a%b)

#OUTPUT
# Enter 1st number:10
# Enter 2nd number:6
# Sum= 16
# Subtraction= 4
# Multiplication= 60
# Division= 1.6666666666666667
# Modulus= 4


# 6.Write a Python program to find the largest of three numbers.

# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# c=int(input("Enter 3rd number:"))
# if a>b and a>c :
#     print(a, " is the largest among",a,",",b,",",c)
# elif b>c : 
#     print(b,"is the largest among",a,",",b,",",c)
# else: 
#     print(c,"is the largest among ",a,",",b,",",c)

# OUTPUT
# Enter 1st number:43
# Enter 2nd number:99
# Enter 3rd number:42
# 99 is the largest among 43 , 99 , 42


# 7.Write a Python program to check whether a given year is a leap year.

# year=int(input("Enter Year:"))
# if year %4 ==0 :
#     print("Given year,",year,",is a leap year")
# else :
#     print("Given year,",year,",is not a leap year ")

# OUTPUT   
# Enter Year:1996
# Given year, 1996 ,is a leap year
# Enter Year:2025
# Given year, 2025 ,is not a leap year 


# 8.Write aPython program to classify a character as vowel or consonant.

# character=str(input("Enter character :"))
# if character=="a" :
#     print(character,"is a vowel")
# elif character== "e" :
#     print(character,"is a vowel")
# elif character=="i" :
#     print(character,"is a vowel")
# elif character =="o" :
#     print(character,"is a vowel")
# elif character=="u" :
#     print(character,"is a vowel")
# else :
#     print(character, "is a consonant")

# OUTPUT
# Enter character :a
# a is a vowel
# Enter character :e
# e is a vowel
# Enter character :t
# t is a consonant


# 9.Write a Python program to calculate grade of a student based on marks (if-elif ladder).

# marks = float(input("enter the marks:"))
# if marks>100:
#     print("Invalid")
# elif marks<0:
#         print("Invalid") 
# elif marks>=90 :
#     print("Grade is A+")
# elif marks>=75 :
#     print("grade is A")
# elif marks>=60 :
#     print("Grade is B")
# elif marks>=40 :
#     print("Grade is C ")
# else :
#     print("Fail")

# OUTPUT
# enter the marks:55.76
# Grade is C 
# enter the marks:97.54
# Grade is A+


# 10.Write a Python program to check whether a number is positive, negative or zero.

# num=float(input("Enter number:"))
# if num >0 :
#     print(num,"is positive")
# elif num <0 :
#     print(num,"is negative")
# else :
#     print("Number is zero")

#OUTPUT
# Enter number:65
# 65.0 is positive
# Enter number:-65.45
# -65.45 is negative
# Enter number:0
# Number is zero


# 11.Write a Python program to display a simple calculator using match-case statement.


# 12.Write a Python program to check whether a number is divided by 3 and 5.

# num=int(input("Enter number:"))
# if num %3==0 and num %5==0 :
#     print("Number(",num,") is divisible by 3 and 5")
# else :
#     print("Number(",num,") is not divisible by 3 and 5")

# OUTPUT 
# Enter number:15
# Number( 15 ) is divisible by 3 and 5
# Enter number:66
# Number( 66 ) is not divisible by 3 and 5


# 13.Write a Python program to print all even numbers between 1 and 100.

# print("Even numbers are:")
# for i in range (2,100,2) :
#     print(i)


# 14.Write a Python program to calculate factorial of a number using while loop.

# n=int(input("Enter number:"))
# fact,i=1,1
# while i<=n:
#     fact*=i
#     i+=1
# print("Factorial is :",fact)

# OUTPUT
# Enter number:5
# Factorial is : 120


# 15.Write a Python program to check whether a number is prime.

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

# OUTPUT
# Enter a number: 45
# 45 is not a prime number.
# Enter a number: 19
# 19 is a prime number.


# 16.Write a Python program to print Fibonacci series up to n terms 

# n=int(input("Enter no of terms:"))

# a=0
# b=1 
# print("Fibonacci series:")
# for i in range (n):
#     print(a)
#     a,b=b,a+b 

# OUTPUT 
# Fibonacci series:
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181


# 17.Write a Python program to find the sum of digits of a given number.


# 18.Write a Python Program to reverse a number using while loop.


# 19.Write a Python program to print a multiplication table of a given number.

# number=int(input("Enter number:"))
# for i in range (1,11) :
#     table = number * i 
#     print(number,"*",i,"=",table)

# OUTPUT
# Enter number:5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50


# 20.Write a Python program to find the GCD/HCF of two numbers.


# 21.Write a Python program to print a half pyramid of * .

# rows = 8
# for i in range (1,rows+1): 
#     for j in range (i,) :
#         print ("*",end=" ")
#     print()  

# OUTPUT
# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *

# 22.Write a Python program to print a inverted half pyramid of * .

# rows = 8
# for i in range (rows+1,0,-1): 
#     for j in range (i) :
#         print ("*",end=" ")
#     print()  

# OUTPUT
# * * * * * * * * * 
# * * * * * * * * 
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# 23.Write a Python program to print a full pyramid of numbers 

# rows = 10 
# for i in range (0,rows): 
#     for j in range (rows-i-1) :
#         print (" ",end=" " )
#     for j in range(2*i+1) :
#         print(i,end=" ")
#     print() 

# OUTPUT
#                   0 
#                 1 1 1 
#               2 2 2 2 2
#             3 3 3 3 3 3 3
#           4 4 4 4 4 4 4 4 4
#         5 5 5 5 5 5 5 5 5 5 5
#       6 6 6 6 6 6 6 6 6 6 6 6 6
#     7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
#   8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9


# 24.Write a Python program to print Floyd's triangle.

# n=int(input("Enter Number:"))
# a=1
# b=1
# for i in range (1,n+1):
#     for j in range(i):
#         print(a,end=" ")
#         a,b=a+1,b+2
#     print()

# OUTPUT
# Enter Number:8
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36

# 25.Write a Python program to print Pascal's triangle.


# 26.Write a Python program to print a diamond pattern of * 

# rows = 10
# for i in range (rows): 
#     for j in range (rows-i-1) :
#         print (" ",end=" " )
#     for j in range(2*i+1) :
#         print(" ",end="*")
#     print()     
# for i in range (rows-1,0,-1): 
#     for j in range (rows-i-1) :
#         print (" ",end=" " )
#     for j in range(2*i+1) :
#         print(" ",end="*")
#     print()       

#OUTPUT
#                    *
#                  * * *
#                * * * * *
#              * * * * * * *
#            * * * * * * * * *
#          * * * * * * * * * * *
#        * * * * * * * * * * * * *
#      * * * * * * * * * * * * * * *
#    * * * * * * * * * * * * * * * * *
#  * * * * * * * * * * * * * * * * * * *
#  * * * * * * * * * * * * * * * * * * *
#    * * * * * * * * * * * * * * * * *
#      * * * * * * * * * * * * * * *
#        * * * * * * * * * * * * *
#          * * * * * * * * * * *
#            * * * * * * * * *
#              * * * * * * *
#                * * * * *
#                  * * *


# 27.Write a Python program to print a hollow square pattern of *.

# 28.Write a python program to find the factorial of a number .

# def factorial(n):
#     if n==0 or n==1 :
#         return 1
#     return  n*factorial(n-1)
# print("factorial of 7 is",factorial(7))

# OUTPUT
# factorial of 7 is 5040


# 29.Write a Python program to check whether a string is palindrome.


# 36.Write a Python program to find the largest element in a list.

# def largest_element(nums):
#     a=list(set(nums))
#     a.sort()
#     if len(a)<2:
#         return None
#     return a[-1]

# nums=[23,49,7,123,79,93,21,443,69]
# print("The largest element is:",largest_element(nums))

# OUTPUT
# The largest element is: 443

# 38.Write a Python program to find the second largest element in list.

# def second_largest(nums):
#     a=list(set(nums))
#     a.sort()
#     if len(a)<2:
#         return None
#     return a[-2]

# nums=[168,20,4,123,78,99,20,34,78]
# print("the second largest is:",second_largest(nums))

# OUTPUT
# the second largest is: 123


# 41.Write a Python program to reverse a list without using reverse() function.

# def reverse_list(ist):
#     return ist[::-1]
# nums=[65,87,34,23,997,54]
# print("Reversed List",reverse_list(nums))

# OUTPUT
# Reversed List [54, 997, 23, 34, 87, 65]

