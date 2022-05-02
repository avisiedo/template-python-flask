from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from api.route.hello import Hello
from api.model.hello import HelloModel

def create_app():

    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'Flask Hello World',
    }
    swagger = Swagger(app)
    api = Api(app)
    api.add_resource(Hello, "/api/hello/<string:name>")

     ## Initialize Config
    app.config.from_pyfile('config.py')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
