t=int(input())
for _ in range(t):
    n=int(input())
    d=input()
    d=list(d)
    for i in range(len(d)):
        if d.count(d[i])==1:
            print(d[i])
            break
    else:
        print(-1)