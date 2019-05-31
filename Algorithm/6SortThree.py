input('请输入三个整数: ')
a=int(input())
b=int(input())
c=int(input())
if a>b:
    t=a
    a=b
    b=t
if b>c:
    t=b
    b=c
    c=t
if a > b:
    t = a
    a = b
    b = t
print('[%s,%s,%s]' % (a,b,c))