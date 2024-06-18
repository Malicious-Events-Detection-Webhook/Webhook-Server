import pickle
import json

filename = 'post-request1718723101.pkl'

deserialized_data = None
with open(filename, 'rb') as f:
    deserialized_data = pickle.load(f)

#pretty_json = json.loads(deserialized_data)

print("action is: ", deserialized_data.keys())
print("the request JSON is: ",json.dumps(deserialized_data, indent=2))
