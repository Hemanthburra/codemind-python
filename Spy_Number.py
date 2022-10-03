n=int(input())
s=0
w=1
while n>0:
    d=n%10
    s+=d
    w*=d
    n=n//10
if s==w:
    print("Spy Number")
else:
    print("Not Spy Number")