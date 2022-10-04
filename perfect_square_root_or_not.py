import math
n=int(input())
d=int(math.sqrt(n))
if n==d*d:
    print(True)
else:
    print(False)