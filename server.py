from flask import Flask, request, jsonify
import json
import pickle as pkl
import os
import time

from events import MaliciousEvents,\
                   RepositoryDeletedEvent, \
                   PushingCode, \
                   HackerTeam, \
                   CheckMaliciousEventTable, \
                   create_malicious_event, \
                   notify_print



""" SAVED_DIR = "."
timestamp = int(time.time())
HTTP_POST_REQUEST = f"post-request{timestamp}.pkl"
os.makedirs(SAVED_DIR, exist_ok=True) """


# def serialize(request):
#     serialized = pkl.dumps(request.json)
#     filename = f"{SAVED_DIR}/{HTTP_POST_REQUEST}"

#     with open(filename, "wb") as f:
#         f.write(serialized)

app = Flask(__name__)

""" @app.route('/', methods=['GET'])
def handle_get():
    # Handle GET request
    print("got a GET request")

    data = {
        "message": "This is a GET response",
        "params": request.args
    }
    return jsonify(data), 200 """

@app.route('/', methods=['POST'])
def handle_post():
    print("got a POST request")
    
    # serialize(request)
    for eventType, isMalicious in CheckMaliciousEventTable.items():
        if isMalicious(request.json):
            event = create_malicious_event(eventType, notify_print, request.json)
            event.notify()

    # pretty_json = json.loads(request.data)
    # print("action is: ", request.json["action"])
    # print("the request JSON is: ",json.dumps(pretty_json, indent=2))
    data = {
        "message": "This is a POST response",
        # "data": request.json
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)














