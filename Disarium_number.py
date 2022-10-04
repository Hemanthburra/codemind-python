n=input()
n1=n
s=0
n=n[::-1]
#print(n)
for i in range(1,len(n)+1):
    d=int(n)%10
    #print(d)
    s+=(d**i)
    #print(s)
    n=int(n)//10
#print(s,n1)
if str(s)==n1:
    print(True)
else:
    print(False)
