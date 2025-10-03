# 23.Write a Python program to print a full pyramid of numbers 

rows = 10 
for i in range (0,rows): 
    for j in range (rows-i-1) :
        print (" ",end=" " )
    for j in range(2*i+1) :
        print(i,end=" ")
    print() 

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