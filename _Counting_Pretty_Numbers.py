def sq(n):
    d=n%10
    if d==2 or d==3 or d==9:
        return True
    else:
        return False
t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    cnt=0
    for i in range(l,r+1):
        if sq(i):
            cnt+=1
    print(cnt)