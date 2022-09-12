s=input()
o=input()
r=list(s)
for i in range(len(r)):
    if r[i]==o:
        print(True)
        print(i)
        break
else:
    print(False)