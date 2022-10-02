n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(len(a)-2):
    if (a[i]%2==0 and a[i+2]%2) or (a[i]%2 and a[i+2]%2==0):
        cnt+=1
print(cnt)
