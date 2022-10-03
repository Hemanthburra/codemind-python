import math
x,y,m=map(int,input().split())
d=math.pow(x,y)
print(int(d%m))