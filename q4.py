n =6
for i in range(n):
    for j in range(i+1):
        if (j%2==1):
            print(j,end=" ")
        else:
            print("*" ,end=" ")
    print()
