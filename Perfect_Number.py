num=int(input())
result=0
for i in range(1,num):
    if (num%i)==0:
        result=result+i
if(result==num):
    print("True")
else:
    print("False")