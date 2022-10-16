n,m=map(int,input().split())
f=[]
ev=0
od=0
for _ in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(len(f)):
    if i%2:
        s=f[i]
        for j in range(len(s)):
            ev+=s[j]
    else:
        s=f[i]
        for j in range(len(s)):
            od+=s[j]
print(od,ev)