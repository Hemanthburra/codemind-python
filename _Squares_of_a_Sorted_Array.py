n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    l.append(a[i]**2)
l.sort()
print(*l)