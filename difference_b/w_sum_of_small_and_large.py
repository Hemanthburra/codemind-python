f=input()
f=f.split()
d=0
d1=0
for i in range(len(f)):
    d+=ord(max(f[i]))
    d1+=ord(min(f[i]))
print(d-d1,end=" ")