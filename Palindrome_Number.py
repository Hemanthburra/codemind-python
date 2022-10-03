t=int(input())
for _ in range(t):
    d=int(input())
    d=list(str(d))
    if d==d[::-1]:
        print(True)
    else:
        print(False)