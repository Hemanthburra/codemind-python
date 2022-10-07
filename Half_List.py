n=int(input())
a=list(map(int,input().split()))
a1=a[n//2:]
a2=a[:n//2]
a1.reverse()
a=a1+a2
print(*a)