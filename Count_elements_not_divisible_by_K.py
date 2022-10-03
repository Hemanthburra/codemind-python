n,k=map(int,input().split())
v=list(map(int,input().split()))
cnt=0
for i in range(len(v)):
    if v[i]%k!=0:
        cnt+=1
print(cnt)