#Depencies
#1.Flask
# sudo pip install Flask
#2.python firebase 1.2
# sudo pip install requests==1.1.0
# sudo pip install python-firebase


from flask import Flask
from flask_restful import Resource, Api
from firebase import firebase

app = Flask(__name__)
api = Api(app)

class status(Resource):
    def get(self):
        return {"status":"ok"}


api.add_resource(status, '/status')


if __name__ == '__main__':
    app.run()