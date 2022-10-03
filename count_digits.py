n=int(input())
s=list(map(int,input().split()))
v=0
f=[]
for i in range(len(s)):
    v=s[i]
    v=list(str(v))
    if v[0]=="-":
        v.pop(0)
    f.append(len(v))
    v=0
print(*f)