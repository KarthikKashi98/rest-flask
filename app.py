
import flask
from flask import request, jsonify
from filelock import Timeout, FileLock
import time

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.debug = True


@app.route('/', methods=['GET'])
def home():
    lock = FileLock("get_id.txt")
    with lock:
        o = open("get_id.txt", "r")
        print(o)
        line = o.readline()
        i = int(line)
        print("before=>", i)
        i += 1


    o.close()
    file = open("get_id.txt", "w")
    file.write(str(i))
    print("after=>", i)
    file.close()
    return jsonify({"given_id": i})

# A route to return all of the available entries in our catalog.
@app.route('/reset', methods=['GET'])
def reset_all():
    lock = FileLock("get_id.txt")
    with lock:
        i = 1


    file = open("get_id.txt", "w")
    file.write(str(i))
    print("after=>", i)
    file.close()
    return jsonify({"given_id": "newly created "})

