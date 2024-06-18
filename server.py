from flask import Flask, request, jsonify

from events import CheckMaliciousEventTable, \
                   event_factory

from notify import notify_print

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    print("got a POST request")
    
    for eventType, isMalicious in CheckMaliciousEventTable.items():
        if isMalicious(request.json):
            event = event_factory(eventType, notify_print, request.json)
            event.Notify()

    data = {
        "message": "This is a POST response",
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

