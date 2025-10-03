# 4.Write a Python program to accept a string and put it in reverse order 

def reverse_string(string):
    return string[::-1]
string=input("Enter String:")
reverse=reverse_string(string)
print("Reverse of the string entered is :",reverse)