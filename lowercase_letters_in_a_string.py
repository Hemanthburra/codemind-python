s=input()
c=0
for i in range(len(s)):
    if s[i].islower():
        c+=1
print(c)