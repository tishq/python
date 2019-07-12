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
        print('查询关键词是'+datav)

        return datav



api.add_resource(BIFunction, '/result')


if __name__ == '__main__':
    app.run(
        # python es_rest.py 可以看到效果(生产环境)
        # host= '0.0.0.0',
        port= 5010,
        debug=True
    )

