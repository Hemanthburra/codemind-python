a,b=map(int,input().split())
d=list(map(int,input().split()))
cnt=0
for i in range(len(d)):
    if d[i]%b==0:
        cnt+=1
print(cnt)