n=int(input())
for _ in range(n):
    d=int(input())
    cnt=1
    #print(d)
    for i in range(1,d+1):
        cnt*=i
    print(cnt)
