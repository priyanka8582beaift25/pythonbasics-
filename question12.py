# 12.Write a Python program to check whether a number is divided by 3 and 5.

num=int(input("Enter number:"))
if num %3==0 and num %5==0 :
    print("Number(",num,") is divisible by 3 and 5")
else :
    print("Number(",num,") is not divisible by 3 and 5")