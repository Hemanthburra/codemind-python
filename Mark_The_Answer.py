n,m=map(int,input().split())
d=list(map(int,input().split()))
val=0
cnt=0
for i in range(len(d)):
    if d[i]<=m:
        val+=1
    else:
        cnt+=1
    if cnt==2:
        break
print(val)
        
        
    
        
