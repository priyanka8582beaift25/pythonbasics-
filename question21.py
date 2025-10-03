# 21.Write a Python program to print a half pyramid of * .

rows = 8
for i in range (1,rows+1): 
    for j in range (i,) :
        print ("*",end=" ")
    print() 