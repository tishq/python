n=int(input())
a=1
b=2
sum=0
for i in range(n):
    sum += (b/a)
    t=a
    a=b
    b=a+t
print(sum)
