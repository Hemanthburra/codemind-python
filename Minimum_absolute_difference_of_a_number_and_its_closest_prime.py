import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
for i in range(n+n):
    if isprime(i):
        l.append(i)
        if i>=n:
            break
if n in l:
    print(n-n)
elif abs(l[-1]-n)>=abs(l[-2]-n):
    print(abs(l[-2]-n))
elif abs(l[-1]-n)<=abs(l[-2]-n):
    print(abs(l[-1]-n))


        