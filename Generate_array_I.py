r=int(input())
f=list(map(int,input().split()))
a,b=[],[]
for i in range(len(f)):
    if i%2:
        b.append(f[i])
    else:
        a.append(f[i])
c=[]
for j in range(len(a)):
    for k in range(0,b[j]):
        c.append(a[j])
print(*c)