# 41.Write a Python program to reverse a list without using reverse() function.

def reverse_list(ist):
    return ist[::-1]
nums=[65,87,34,23,997,54]
print("Reversed List",reverse_list(nums))