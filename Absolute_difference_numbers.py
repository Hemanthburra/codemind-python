x,y=map(int,input().split())
x=list(str(x))
e=x[:y]
e1=x[-y:]
e=int("".join(e))
e1=int("".join(e1))
print(abs(e-e1))