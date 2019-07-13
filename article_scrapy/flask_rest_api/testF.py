import math

data = "406 1764.2 11.5 775 1682.9 20.1 920 2291.6 38.1"

def getResult(data):
    lists = data.split()
    n = len(lists)

    # 求出有几组数据
    line = n // 3

    # 取对数后的f,p,q
    lf = []
    lp = []
    lq = []

    for i in range(n):
        if i % 3 == 0:
            a = math.log(float(lists[i]))
            lf.append(a)
        elif i % 3 == 1:
            b = math.log(float(lists[i]))
            lp.append(b)
        else:
            c = math.log(float(lists[i]))
            lq.append(c)

    ff = []
    pp = []
    fp = []
    fq = []
    pq = []
    for i in range(line):
        ff.append(lf[i] * lf[i])
        pp.append(lp[i] * lp[i])
        fp.append(lf[i] * lp[i])
        fq.append(lf[i] * lq[i])
        pq.append(lp[i] * lq[i])

    # 求出正则方程组需要的数据
    fa = 0.0
    pa = 0.0
    qa = 0.0
    ffa = 0.0
    ppa = 0.0
    fpa = 0.0
    fqa = 0.0
    pqa = 0.0
    for i in range(line):
        fa += lf[i]
        pa += lp[i]
        qa += lq[i]
        ffa += ff[i]
        ppa += pp[i]
        fpa += fp[i]
        fqa += fq[i]
        pqa += pq[i]

    # 高斯列主元消去法解正则方程组
    left = [[line,fa,pa],[fa,ffa,fpa],[pa,fpa,ppa]]
    right = [qa,fqa,pqa]


    # 找到每一列中最大的元素
    for k in range(line-1):
        v = 0
        row = 0
        for i in range(k,line):
            if math.fabs(left[i][k])>v:
                v = left[i][k]
                col = k
                row = i

        # 不能求解
        if left[row][row] == 0:
            print("NO")
            return "NO"


        print("交换前")
        print(left)
        print(right)

        # 交换
        if row!=k:
            t = left[k]
            left[k] = left[row]
            left[row] = t

            tt = right[k]
            right[k] = right[row]
            right[row] = tt

        print("交换后")
        print(left)
        print(right)

        # 消元
        c = [0,0,0]
        for j in range(k+1,line):
            c[j]=left[j][k]/left[k][k]
        print("消元因子")
        print(c)
        for i in range(k+1,line):
            for j in range(line):
                left[i][j] = left[i][j] - c[i]*left[k][j]
            right[i] = right[i] - c[i]*right[k]
        print("消元后")
        print(left)
        print(right)


    # 回代求解
    x = [0,0,0]
    x[line-1] = right[line-1]/left[line-1][line-1]

    for i in range(line-2,-1,-1):
        sum = 0
        for j in range(i+1,line):
            sum+=(left[i][j]*x[j])
        x[i] = (right[i] - sum)/left[i][i]
    x[0] = math.exp(x[0])
    print(x)







getResult(data)





