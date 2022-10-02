def pronic(n):
    for i in range(n-1):
        if i*(i+1)==n:
            return True
    return False
a=int(input())
if pronic(a):
    print("YES")
else:
    print("NO")