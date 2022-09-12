t=['a','e','i','o','u','A','E','I','O','U']
s=input()
u=[]
for i in range(len(s)):
    if s[i] not in u and s[i] in t:
        u.append(s[i])
if len(u)==0:
    print(-1)
else:
    print(*u)