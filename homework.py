# To print reverse numbers from n to 1 
# n = int(input("Enter num:"))
# for i in range (n,0,-1) :
    # print(i)



# Sum of the first n natural numbers 

# n = int(input("enter n:"))
# if n<=0 :
    # print("Please enter a number greater than 0")
# else :
    # total= n*(n+1)//2
    # print("Sum of natural numbers is :",total )



# Sum of the first n natural numbers

# n = int(input("enter n:"))
# sum = 0
# for i in range (1,n+1) :
    # sum += i
# print("Sum of natural numbers is :",sum)



# To Count the number of digits in a given number

num = int(input("enter n:"))
num_str = str(num)
i= 0
for _ in num_str :
    i = i + 1 
print("Number of digits are:",i)