def primes(n):
    if n==1:
        return False
    for j in range(2,n):
        if n%j==0:
            return False
    return True
p=int(input())
n=list(map(int,input().split()))
cnt=0
s=0
for i in range(p):
    if primes(n[i]):
        cnt+=1
        s+=n[i]
a=s/cnt
print("{0:.2f}".format(a))