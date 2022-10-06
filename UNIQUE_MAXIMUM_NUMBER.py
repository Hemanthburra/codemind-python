n=int(input())
a=list(map(int,input().split()))
cnt=0
l=[]
for i in range(len(a)):
    if a.count(a[i])==1:
        if cnt<a[i]:
            cnt=a[i]
if cnt==0:
    print(-1)
else:
    print(cnt)