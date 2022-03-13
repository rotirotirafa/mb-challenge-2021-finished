from flask import Flask, jsonify
from flask_swagger import swagger

from app.settings import HOST, PORT
from app.utils.urls import build_urls


def create_app():
    application = Flask(__name__)
    build_urls(application)
    return application


app = create_app()


@app.route("/")
def base():
    return jsonify({'message': 'Hello!'})


@app.route("/swagger")
def swagger_route():
    return jsonify(swagger(app))


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
