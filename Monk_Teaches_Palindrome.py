n=int(input())
for _ in range(n):
    s=input()
    if s==s[::-1]:
        if len(s)%2:
            print("YES ODD")
        else:
            print("YES EVEN")
    else:
        print("NO")