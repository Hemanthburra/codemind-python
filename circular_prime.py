import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=input()
#print(isprime(int(n)),isprime(int(n[::-1])))
if isprime(int(n)) and isprime(int(n[::-1])):
    print("circular prime")
elif isprime(int(n)) or isprime(int(n[::-1])):
    print("prime but not a circular prime")
else:
    print("not prime")
        