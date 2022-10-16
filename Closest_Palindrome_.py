def palin(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False

n=int(input())
l=[]
for i in range(n+n):
    if palin(i):
        l.append(i)
        if i>n:
            break
if n in l:
    l.remove(n)
if abs(l[-1]-n)>abs(l[-2]-n):
    print(l[-2])
elif abs(l[-1]-n)<abs(l[-2]-n):
    print(l[-1])
elif abs(l[-1]-n)==abs(l[-2]-n):
    print(l[-2],l[-1])