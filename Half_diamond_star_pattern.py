n=int(input())
if n<3:
    print("The pattern is not possible")
else:
    
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*",end="")
        print()