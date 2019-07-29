n=int(input())


q=0
for m in range(0,n):
 p=1
 for o in range(1,m+1):
  p=p*(o+1)
 q=q+p

print(q)


