n=int(input())
j=list(map(int,input().split()))
cnt=0
k=0
for i in range(len(j)):
    if j[i]%2==0 and i%2==0:
        cnt+=1
    if j[i]%2==0:
        k+=1
if cnt==k:
    print(True)
else:
    print(False)