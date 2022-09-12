s=input()
t=['a','e','i','o','u','A','E','I','O','U']
s=s.split()
#print(s)
y=[]
for i in range(len(s)):
    p=s[i]
    #print(p)
    c=0
    for j in range(len(p)):
        #print(p[i])
        if p[j] in t:
            c+=1
    y.append(c)
print(min(y))