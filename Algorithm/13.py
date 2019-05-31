n=int(input())
a=(n%10+5)%10  #个
b=(int(n/10)%10+5)%10  #十
c=(int(n/100)%10+5)%10 #白
d=(int(n/1000)+5)%10 #千

aa=[a,b,c,d]
for i in range(4):
 print(aa[i],end='')
