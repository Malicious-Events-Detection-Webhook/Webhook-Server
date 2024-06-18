import pickle
import json
from datetime import datetime, time     # for IsPushedEvent
from dateutil import parser             # for IsDeletedAfter10Min
filename = 'post-request.pkl'

def IsAddedHackerTeam(json_data):
    try:
        return  json_data["action"] == "added" \
            and json_data["scope"] == "team" \
            and json_data["team"]["name"][:6].lower() == "hacker"
    except:
        return False
        
def IsPushedEvent(json_data):
    try:
        
        timestamp_pushed_at = json_data["repository"]["pushed_at"]
        date = datetime.fromtimestamp(timestamp_pushed_at)
        print(date, date.hour)
        start_time = time(14, 0)  
        end_time = time(16, 0)
        return (start_time <= date.time()<= end_time)
    except:
        return False


def IsDeletedAfter10Min(json_data):
    try:
        if json_data["action"] == "deleted":

            date_deleted_str = json_data["repository"]["updated_at"]
            date_created_str = json_data["repository"]["created_at"]
            created_at = parser.isoparse(date_created_str)
            deleted_at = parser.isoparse(date_deleted_str)

            # Calculate the time difference
            time_difference = deleted_at - created_at

            # Check if the difference is less than 10 minutes
            return time_difference.total_seconds() < 600
        else:
            return False
    except:
        return False


deserialized_data = None
with open(filename, 'rb') as f:
    deserialized_data = pickle.load(f)

#pretty_json = json.loads(deserialized_data)

print("action is: ", deserialized_data.keys())
#print("the request JSON is: ",json.dumps(deserialized_data, indent=2))

if IsAddedHackerTeam(deserialized_data):
    print("Hacker team added")
else:
    print("Hacker team not added")

if IsPushedEvent(deserialized_data):
    print("Pushed event")
else:
    print("Not pushed event")