n=int(input())
j=list(str(n))
cnt=0
#print(n)
for i in range(len(j)):
    if int(j[i])%2==0:
        cnt+=1
if cnt==len(j):
    print("Even")
elif cnt==0:
    print("Odd")
else:
    print("Mixed")