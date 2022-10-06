import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
t=int(input())
e=int(input())
f=0
for i in range(1,10):
    f=t+e+i
    if isprime(f):
        print(i)
        break
    

        