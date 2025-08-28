# for i in range (1,4):
    # for j in range(1,4):
        # print(i*j,end=" ")
    # print()




# rows = 5
# for i in range (1,rows+1): 
    # for j in range (i):
        # print (1,end=" ")
    # print()
    
#rows = 5
#for i in range (1,rows+1): 
    #for j in range (i):
        # print (2,end=" ")
    # print()
    
    
    
#rows = 5
#for i in range (1,rows+1): 
    #for j in range (i):
        #print (i,end=" ")
    #print()
    
    
# rows = 8 
# for i in range (1,rows+1) :
    # # j in range (i) :
        # print(j+i,end=" ")
    # print()  
    
    

# rows = 5
# for i in range (rows+1,0,-1): 
    # for j in range (i) :
        # print ("*",end=" ")
    # print()              
    
    
#rows = 5
# for i in range (1,rows+1): 
    # for j in range (i,) :
        # print ("*",end=" ")
    # print()    
    
    

rows = 10
for i in range (rows): 
    for j in range (rows-i-1) :
        print (" ",end=" " )
    for j in range(1*i+1) :
        print(" ",end="*")
    print()            