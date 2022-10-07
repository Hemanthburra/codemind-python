n=int(input())
a=list(map(int,input().split()))
ev=0
od=0
for i in range(len(a)):
    if a[i]%2==0:
        ev+=1
    else:
        od+=1
print(ev,od)