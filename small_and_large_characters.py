n=input()
n=n.split()
for i in range(len(n)):
    print(min(n[i]),max(n[i]),end=" ")
