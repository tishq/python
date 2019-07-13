import math

# data = "406 1764.2 11.5 775 1682.9 20.1 920 2291.6 38.1"

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

    # 正则方程组m*m
    m=3

    # 找到每一列中最大的元素
    for k in range(m-1):
        v = 0
        row = 0
        for i in range(k,m):
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
        c = [0]*m
        for j in range(k+1,m):
            c[j]=left[j][k]/left[k][k]
        print("消元因子")
        print(c)
        for i in range(k+1,m):
            for j in range(m):
                left[i][j] = left[i][j] - c[i]*left[k][j]
            right[i] = right[i] - c[i]*right[k]
        print("消元后")
        print(left)
        print(right)


    # 回代求解
    x = [0]*m
    x[m-1] = right[m-1]/left[m-1][m-1]

    for i in range(m-2,-1,-1):
        sum = 0
        for j in range(i+1,m):
            sum+=(left[i][j]*x[j])
        x[i] = (right[i] - sum)/left[i][i]
    x[0] = math.exp(x[0])
    print(x)
    return x



# flask restfull
from flask import Flask, render_template, make_response
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

# 利用reqparse简化带参数的请求
parser = reqparse.RequestParser()
parser.add_argument('data')

# 二元冥函数回归分析
class BIFunction(Resource):
    def post(self):
        # 拿到post里面设置的args
        data = parser.parse_args()
        # 取出args里面对应的值
        datav = data['data']
        print('数据:'+datav)

        results = getResult(datav)

        return make_response(render_template('index.html',results=results))



api.add_resource(BIFunction, '/result')


if __name__ == '__main__':
    app.run(
        # python es_rest.py 可以看到效果(生产环境)
        # host= '0.0.0.0',
        port= 5010,
        debug=True
    )

