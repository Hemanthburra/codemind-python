import math
n=int(input())
a=list(map(int,input().split()))
a.sort()
s=0
l=[]
for i in range(len(a)):
    l.append(int(math.sqrt(a[i])))
for j in range(len(l)):
    if l[j]*l[j]==a[j]:
        s+=a[j]
print(s)