t=['a','e','i','o','u','A','E','I','O','U']
s=input()
s=s.split()
cnt=0
for i in range(len(s)):
    r=s[i]
    if r[0] in t and r[-1] not in t:
        cnt+=1
print(cnt)