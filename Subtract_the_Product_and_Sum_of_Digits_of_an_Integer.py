n=int(input())
g=0
s=1
while n>0:
    d=n%10
    g+=d
    s*=d
    n=n//10
print(s-g)