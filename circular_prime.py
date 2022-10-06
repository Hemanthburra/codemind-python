import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
t=int(input())
e=str(t)
e=int(e[::-1])
if isprime(t) and isprime(e):
    print("circular prime")
elif isprime(t) or isprime(e):
    print("prime but not a circular prime")
else:
    print("not prime")
        
    

        