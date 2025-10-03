# 22.Write a Python program to print a inverted half pyramid of * .

rows = 8
for i in range (rows+1,0,-1): 
    for j in range (i) :
        print ("*",end=" ")
    print()  

# OUTPUT
# * * * * * * * * * 
# * * * * * * * * 
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *