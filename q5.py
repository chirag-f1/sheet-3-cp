n =5
for i in range(n):
    for j in range (n):
        if (j ==0 or j==4):
            print("*",end=" ")
        else:
            print("_" ,end=" ")
    print()
