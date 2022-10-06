n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(len(a)):
    d=list(str(a[i]))
    if len(d)%2==0:
        cnt+=1
print(cnt)