n=int(input())
d1=n
n=abs(n)
g=0
while n>0:
    d=n%10
    g=(g*10)+d
    n=n//10
if d1<0:
    print(0-g)
else:
    print(g)
    