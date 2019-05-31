n=int(input())
ht=0
hn=100
for i in range(n):
    hn = hn / 2
    if i==0:
        ht=100
    else:
        ht+=hn*2*2
print('总高度:tour =%s' %(ht))
print('第 %s 次反弹高度:height =%s' %(n,hn))