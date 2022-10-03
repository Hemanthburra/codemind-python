n=int(input())
v=list(map(int,input().split()))
f=[]
s=0
for i in range(len(v)):
    while v[i]>0:
        d=v[i]%10
        s=(s*10)+d
        v[i]=v[i]//10
    f.append(s)
    s=0
print(*f)