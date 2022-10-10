n=int(input())
for _ in range(n):
    s=input()
    d=0
    for i in range(len(s)):
        if s[i].isnumeric():
            d+=1
    if d!=0:
        print("Yes")
    else:
        print("No")