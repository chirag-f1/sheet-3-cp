n = 6
for i in range(n):
    for j in range(1):
        print("*" ,end=" ")
    for j in range(i+1,n):
        print("_",end=" ")
    for j in range(1):
        print("*",end=" ")
    print()
