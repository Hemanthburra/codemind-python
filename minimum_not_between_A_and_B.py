x=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
for i in range(len(s)):
    if s[i]<a:
        d.append(s[i])
    if s[i]>b:
        d.append(s[i])

if(len(d)==0):
    print("-1")
else:
    print(min(d))
    