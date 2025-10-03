# 36.Write a Python program to find the largest element in a list.

def largest_element(nums):
    a=list(set(nums))
    a.sort()
    if len(a)<2:
        return None
    return a[-1]

nums=[23,49,7,123,79,93,21,443,69]
print("The largest element is:",largest_element(nums))