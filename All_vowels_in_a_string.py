t=['a','e','i','o','u']
s=input()
o=[]
for i in range(len(s)):
    if s[i] in t:
        o.append(s[i])
o=set(o)
#print(o)
if len(o)==len(t):
    print(True)
else:
    print(False)