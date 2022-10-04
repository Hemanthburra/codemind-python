import math
n,m=map(int,input().split())
while n!=0:
    if n>m:
        n,m=m,n
    else:
        m=m-n
print(m)