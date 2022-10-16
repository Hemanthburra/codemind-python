n,m=map(int,input().split())
f=[]
ev=0
od=0
for _ in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(len(f)):
    s=f[i]
    for j in range(len(s)):
        if s[j]%2==0:
            ev+=s[j]
        else:
            od+=s[j]
print(ev,od)