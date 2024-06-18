import pickle
import json

filename = 'post-request.pkl'

with open(filename, 'rb') as f:
    deserialized_data = pickle.load(f)

pretty_json = json.loads(request.data)
print("action is: ", request.json["action"])
print("the request JSON is: ",json.dumps(pretty_json, indent=2))
 


print(f"Deserialized data: {deserialized_data}")
