# flask restfull
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource



app = Flask(__name__)
api = Api(app)






class ArticlesR(Resource):
    def get(self,userId):
        # userId = int(parser.parse_args()['userId'])
        print(userId)
        print(type(userId))

        return userId

api.add_resource(ArticlesR, '/articles/<userId>')

if __name__ == '__main__':
    app.run(
        # python es_rest.py 可以看到效果(生产环境)
        host= '0.0.0.0',
        port= 5009,
        debug=True
    )
