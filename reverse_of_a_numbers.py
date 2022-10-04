n=int(input())
s=""
while n>0:
    d=n%10
    s+=str(d)
    n=n//10
print(s)