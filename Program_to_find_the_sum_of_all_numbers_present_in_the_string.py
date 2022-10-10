s=input()
k=0
for i in range(len(s)):
    if s[i].isnumeric():
        k+=int(s[i])
print(k)