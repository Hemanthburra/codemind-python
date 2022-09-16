t=int(input())
for i in range(t):
    n=int(input())
    f=list(map(int,input().split()))
    g=f.copy()
    f.sort()
    if g==f:
        print(0)
    else:
        print(max(f)-min(f))