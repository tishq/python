import math

data = "1 2.0 3 4 5.9 6 7 8 9"

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






getResult(data)


