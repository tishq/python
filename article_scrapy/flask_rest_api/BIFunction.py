import math
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


# flask restfull
from flask import Flask
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

        result = getResult(datav)

        return result



api.add_resource(BIFunction, '/result')


if __name__ == '__main__':
    app.run(
        # python es_rest.py 可以看到效果(生产环境)
        # host= '0.0.0.0',
        port= 5010,
        debug=True
    )

