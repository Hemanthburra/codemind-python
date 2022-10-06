n=int(input())
l=list(map(int,input().split()))
d=int(input())
h=max(l)
g=[]
for i in range(len(l)):
    if l[i]+d>=h:
        g.append("True")
    else:
        g.append("False")
print(*g)