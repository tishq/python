
n = int(input('整数 n 为:'))
m = int(input('向后移 m 个位置为:'))
number = list(map(int, input().strip().split())) #以空格输入若干数据存入列表
i=0
k=0
list2=[]
for num in number:
    list2.append(number[0])
    k=k+1
for num in number:
  if i+m>=n:
     j=i+m-n
     list2[j]=number[i]
  else :
     list2[i+m]=number[i]
  i=i+1
print(list2)
