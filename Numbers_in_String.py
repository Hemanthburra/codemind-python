s=input()
cnt=0
for i in range(len(s)):
    if s[i].isnumeric():
        cnt+=int(s[i])
print(cnt)