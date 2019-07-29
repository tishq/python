dat = input('请输入年月日: ')
y,m,d=map(int,dat.split()) # 获取年月日

ly = False
if y%100 == 0: # 若年份能被100整除
    if y%400 == 0: # 且能被400整除
        ly = True # 则是闰年
    else:
        ly = False
elif y%4 == 0: # 若能被4整除
     ly = True # 则是闰年
else:
    ly = False

if ly == True: # 若是闰年，则二月为29天
    ms = [31, 29, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
else:
    ms = [31, 28, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
days = 0

for i in range(1,13): # 从1到12判断，已确定月份
    if i == m:
        for j in range(i-1): # 确定月份i之后，则将ms列表中的前i-1项相加
           days += ms[j]
        print('It is the %sth day.' % ((days +d)))