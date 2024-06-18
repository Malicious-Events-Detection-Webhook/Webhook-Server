from flask import Flask, request, jsonify

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
    print("the request JSON is: ", request.json)
    data = {
        "message": "This is a POST response",
        "data": request.json
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)














