from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

from resources.item import ItemList, Item

app = Flask(__name__)
app.secret_key = "TheBestKeptSecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWT(app, authenticate, identity)
api = Api(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, "/items")

if __name__ == "__main__":
    from db import db
    db.init_app(app)

    app.run(port = 5000, debug = True)
