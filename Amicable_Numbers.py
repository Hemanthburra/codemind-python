a=int(input())
b=int(input())
f=[]
f1=[]
for i in range(1,a//2+1):
    if a%i==0:
        f.append(i)
for j in range(1,b//2+1):
    if b%j==0:
        f1.append(j)
if sum(f1)==a and sum(f)==b:
    print("Amicable")
else:
    print("Not Amicable")