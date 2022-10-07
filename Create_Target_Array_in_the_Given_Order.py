n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    l.insert(b[i],a[i])
print(*l)