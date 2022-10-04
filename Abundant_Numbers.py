#import math
n=int(input())
s=0
#print(int(math.sqrt(n)))
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
#print(s,n)
if s>n:
    print(True)
else:
    print(False)