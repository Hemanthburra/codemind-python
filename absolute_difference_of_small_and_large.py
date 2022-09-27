f=input()
f=f.split()
for i in range(len(f)):
    print(abs(ord(max(f[i]))-ord(min(f[i]))),end=" ")