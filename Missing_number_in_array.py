n=int(input())
for _ in range(n):
    y=int(input())
    d=list(map(int,input().split()))
    d.sort()
    #print(d)
    for i in range(1,y):
        if i!=d[i-1]:
            print(i)
            break
    else:
        print(y)
    