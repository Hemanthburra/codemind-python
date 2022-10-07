n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    #print(a.count(a[i]),n//2)
    if a.count(a[i])==(n//2+1):
        print(a[i])
        break