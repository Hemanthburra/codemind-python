import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
t=int(input())
t1=int(input())
for i in range(t,t1+1):
    if isprime(i):
        print(i)
    

        