# 38.Write a Python program to find the second largest element in list.

def second_largest(nums):
    a=list(set(nums))
    a.sort()
    if len(a)<2:
        return None
    return a[-2]

nums=[168,20,4,123,78,99,20,34,78]
print("the second largest is:",second_largest(nums))