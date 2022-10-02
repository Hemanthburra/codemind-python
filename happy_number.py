def happy(num):
    l=[]
    while num not in l:
        l.append(num)
        num=sum([int(d)**2 for d in str(num)])
    if 1 in l:
        return True
    else:
        return False
a=int(input())
if happy(a):
    print(True)
else:
    print(False)