n,m=map(int,input().split())
d=list(map(int,input().split()))
for i in range(m):
    d.append(d[0])
    d.pop(0)
    #print(d)
print(*d)