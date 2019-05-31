n=int(input())
a=0
b=1
m=0
for m in range(0,n):
 n=n-1
 if n==0:
    print(b)
 else:
    print(b,end=',')
 c=a
 a=b
 b=a+c
