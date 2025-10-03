rows = 10
for i in range (rows): 
    for j in range (rows-i,1,+7) :
        print (" ",end=" " )
    for j in range(1*i+1) :
        print(" ",end="*")
    print()   