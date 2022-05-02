from http import HTTPStatus
from flask import Blueprint
from flask_restful import Resource
from flasgger import swag_from
from api.model.hello import HelloModel
from api.schema.hello import HelloSchema

# https://github.com/flasgger/flasgger#using-flask-restful-resources

# hello_api = Blueprint('api', __name__)


class Hello(Resource):
    def __init__(self):
        pass

    def get(self, name):
        """
        Hello world get example
        ---
        parameters:
        - in: path
          name: name
          type: string
          required: true
          default: World
        responses:
          "200":
            description: A single hello world item
            schema:
              id: hello
              properties:
                name:
                  type: string
                  description: The hello world message
                  default: "Hello World!"
        """
        obj = HelloModel(name)
        return {'message': obj.message}, 200

    def post(self):
        pass

    def put(self):
        pass

    def delete(selg):
        pass
