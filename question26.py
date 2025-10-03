# 26.Write a Python program to print a diamond pattern of * 

rows = 10
for i in range (rows): 
    for j in range (rows-i-1) :
        print (" ",end=" " )
    for j in range(2*i+1) :
        print(" ",end="*")
    print()     
for i in range (rows-1,0,-1): 
    for j in range (rows-i-1) :
        print (" ",end=" " )
    for j in range(2*i+1) :
        print(" ",end="*")
    print()     