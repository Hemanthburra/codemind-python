n=int(input())
f=list(map(int,input().split()))
s=""
for i in range(len(f)):
    s+=str(f[i])
s=int(s)
s=s+1
s=list(str(s))
print(*s)