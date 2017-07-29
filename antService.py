#Depencies
#1.Flask
# sudo pip install Flask

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class status(Resource):
    def get(self):
        return {"status":"ok"}


api.add_resource(status, '/status')


if __name__ == '__main__':
    app.run()