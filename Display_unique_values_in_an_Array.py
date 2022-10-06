n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(len(l)):
    if l.count(l[i])==1:
        print(l[i],end=" ")
        cnt=1
if cnt==0:
    print(-1)