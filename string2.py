# def find_duplicates(s):
#     seen=set[s]
#     for ch in s :
#         if ch in seen:
#             return ch 
#         else :
#             return 0
# user=input("Enter your value:")
# duplicates=find_duplicates(user)
# if duplicates :
#     print("duplicate is found ")
# else: 
#     print("Duplicate not found")



from collections import Counter 
def find_all_duplicates(s):
    freq=Counter(s)
    duplicates={ch:count for ch,count in freq.items() if count>1}
    return duplicates
user=input("Enter your name:")
duplicates=find_all_duplicates(user)
if duplicates:
    print("Duplicate character with counts:")
    for ch,count in duplicates.items():
        print(f"{ch}...{count} times")
else:
    print("No duplicate character found")