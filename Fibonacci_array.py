n=int(input())
f=list(map(int,input().split()))
cnt=0
if len(f)<=2:
    print("no")
else:
    for i in range(len(f)-2):
        if f[i]+f[i+1]!=f[i+2]:
            cnt=1
            break
    if cnt==1:
        print("no")
    else:
        print("yes")
    
