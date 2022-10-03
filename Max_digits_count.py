n=int(input())
f=list(map(int,input().split()))
v=(len(str(max([abs(element) for element in f]))))
cnt=0
for i in range(len(f)):
    f1=str(f[i])
    if v==len(f1):
        cnt+=1
print(cnt)