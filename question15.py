# 15.Write a Python program to check whether a number is prime.

num = int(input("Enter a number: "))
#Prime numbers are greater than 1
if num <= 1:
    print(num, "is not a prime number.")
else:
    i = 2
    while i < num:
        if num % i == 0:
            print(num, "is not a prime number.")
            break
        i += 1
    else:
        print(num, "is a prime number.")