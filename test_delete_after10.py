import json
from dateutil import parser             # for IsDeletedAfter10Min

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




# Assuming your JSON file is named 'data.json' and it's in the current directory
file_name = 'deleted.json'



# Open the file for reading
with open(file_name, 'r') as file:
    # Load the JSON data
    data = json.load(file)
    if IsDeletedAfter10Min(data):
        print("Hacker team deleted")
    else:
        print("Hacker team not deleted")


