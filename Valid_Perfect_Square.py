n=int(input())
import math
for _ in range(n):
    d=int(input())
    d1=int(math.sqrt(d))
    if d==d1*d1:
        print(True)
    else:
        print(False)