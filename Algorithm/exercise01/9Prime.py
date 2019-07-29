m,n = eval(input('请输入 m 和 n:'))
flag = 1
prime = []

if m<3:
    m=3
    prime.append(2)

for p in range(m,n):
    for i in range(2,p-1):
        if(p%i==0):
            flag = 0
    if flag == 1:
        prime.append(p)
    else:
        flag = 1
for p in prime:
    print(p)
print('The total is %s' %(len(prime)))