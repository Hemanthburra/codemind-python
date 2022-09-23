t=int(input())
t=list(str(t))
r=t.copy()
t=set(t)
#print(t,r)
if len(r)==len(t):
    print("Unique Number")
else:
    print("Not Unique Number")