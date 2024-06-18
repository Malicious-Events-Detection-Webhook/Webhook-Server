from datetime import datetime, time     # for IsPushedEvent
from dateutil import parser             # for IsDeletedAfter10Min

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

            time_difference = deleted_at - created_at

            return time_difference.total_seconds() < 600
        else:
            return False
    except:
        return False
