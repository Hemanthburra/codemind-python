n=int(input())
a=list(map(int,input().split()))
cnt=0
cnt1=0
for i in range(len(a)):
    if i%2==0:
        cnt+=a[i]
    else:
        cnt1+=a[i]
if (cnt-cnt1)==0:
    print("YES")
else:
    print("NO")