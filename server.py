from flask import Flask, request, jsonify
import json
import pickle as pkl
import os

SAVED_DIR = "."
HTTP_POST_REQUEST = "post-request.pkl"
os.makedirs(SAVED_DIR, exist_ok=True)

def serialize(request):
    serialized = pkl.dumps(request)
    filename = f"{SAVED_DIR}/{HTTP_POST_REQUEST}"

    with open(filename, "wb") as f:
        f.write(serialized)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    # Handle GET request
    print("got a GET request")

    data = {
        "message": "This is a GET response",
        "params": request.args
    }
    return jsonify(data), 200

@app.route('/', methods=['POST'])
def handle_post():
    # Handle POST request
    print("got a POST request")
    
    serialize(request)

    pretty_json = json.loads(request.data)
    print("action is: ", request.json["action"])
    print("the request JSON is: ",json.dumps(pretty_json, indent=2))
    data = {
        "message": "This is a POST response",
        "data": request.json
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)














