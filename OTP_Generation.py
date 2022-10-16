s=input()
k=""
for i in s:
    if int(i)&1:
        k+=str(int(i)**2)
print(k)