n=int(input())
b=list(map(int,input().split()))
if (all(i < j for i, j in zip(b,b[1:]))):
    print("yes")
else:
    print("no")
