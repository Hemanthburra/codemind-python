n=int(input())
v=list(map(int,input().split()))
x=0
for i in range(len(v)):
    while v[i]>0:
        d=v[i]%10
        x+=d
        v[i]=v[i]//10
print(x)