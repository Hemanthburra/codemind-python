t=int(input())
for _ in range(t):
    d=input()
    cnt=0
    d=list(d)
    d.sort()
    #print(d)
    for i in range(len(d)-1):
        if abs(int(d[i])-int(d[i+1]))==1:
            cnt+=1
    #print(cnt,d)
    if cnt==len(d)-1:
        print("YES")
    else:
        print("NO")