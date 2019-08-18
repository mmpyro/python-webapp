from flask import Flask, request, abort, make_response, jsonify
import os
app = Flask(__name__)
version = '2.0.1'

@app.route("/")
def home():
    return version

@app.route("/data", methods=['POST'])
def save_data():
    content = request.json
    storage_path = os.environ['WEB_APP_STORAGE']
    if not content['msg']:
        return abort(400)
    else:
        with open(os.path.join(storage_path, 'data.txt'), 'a+') as file:
            file.write(content['msg']+'\n')
        return make_response('added', 201)

@app.route("/data", methods=['GET'])
def read_data():
    storage_path = os.environ['WEB_APP_STORAGE']
    path = os.path.join(storage_path, 'data.txt')
    if os.path.exists(path):
        with open(path, 'r') as file:
            lines = file.readlines()
        return make_response(jsonify(lines), 200)
    return abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)