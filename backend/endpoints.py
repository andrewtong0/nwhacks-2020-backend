import os
import database.db as dtb
from backend.encoder import JSONEncoder

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template()

@app.route("/api/create-account", methods=["PUT"])
def create_account():
    '''
    {
        first_name: string,
        last_name: string,
        reddit_name: string
    }
    '''
    content = request.json
    if ('first_name' in content and 'last_name' in content and 'reddit_name' in content):
        dtb.addUser(content['first_name'], content['last_name'], content['reddit_name'])
        newUser = dtb.myuser.find_one({'name': content['first_name'] + ' ' + content['last_name']})
        return JSONEncoder().encode(newUser)
    return 'Cannot find keys required to create account', 400


@app.route("/api/<string:first_name>/<string:last_name>", methods=['GET'])
def home(first_name, last_name):
    x = dtb.myuser.find_one({'name': first_name + ' ' + last_name})
    return JSONEncoder().encode(x)


@app.route("/api/<string:reddit_name>", methods=['POST'])
def get_reddit_info(reddit_name):
    dtb.getRedditContent(reddit_name)
    user = dtb.myuser.find_one({'reddit_name': reddit_name})
    return JSONEncoder().encode(user)


if __name__ == "__main__":
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
