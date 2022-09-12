t=['a','e','i','o','u']
s=input()
s=list(s)
#print(s)
for i in range(len(s)):
    if s[i] in t:
        t.remove(s[i])
if len(t)==0:
    print("0")
else:
    print(*t)