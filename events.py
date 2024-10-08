from abc import ABC, abstractmethod
from datetime import datetime     # for IsPushedEvent
from colorama import Fore, Style

from check_mallicious import IsPushedEvent, \
                             IsDeletedAfter10Min, \
                             IsAddedHackerTeam
CheckMaliciousEventTable = {
    "RepositoryDeletedEvent" : IsDeletedAfter10Min,
    "PushingCode" : IsPushedEvent,
    "HackerTeam" : IsAddedHackerTeam
}

class MaliciousEvents(ABC):
    def __init__(self, notify):
        self.notify = notify
        self.data = {}
        self.malicious_events_type = ""

    def Notify(self):
        self.notify(self.to_string())

    @abstractmethod
    def to_string(self):
        pass

class RepositoryDeletedEvent(MaliciousEvents):
    def __init__(self, notify, data):
        super().__init__(notify)
        self.malicious_events_type = "\'Repository Deleted less than 10 minutes after creating\'"
        self.data = {
            "full_name" : data["repository"]["full_name"],
            "created_at" : data["repository"]["created_at"],
            "deleted_at" : data["repository"]["updated_at"]
        }


    def to_string(self):
        return "Malicious event of type: " + Fore.RED + self.malicious_events_type \
            + Fore.WHITE \
            +   " is detected ! \n" \
            + "The repository named: " + self.data["full_name"] \
            + "\ncreated at: " + self.data["created_at"] \
            + "\nwas deleted at: " + self.data["deleted_at"]

class PushingCode(MaliciousEvents):
    def __init__(self, notify, data):
        super().__init__(notify)
        self.malicious_events_type = "\'Code pushed between 14:00 and 16:00\'"
        self.data = {
            "full_name" : data["repository"]["full_name"],
            "pusher" : data["pusher"],
            "pushed_at" : datetime.fromtimestamp(data["repository"]["pushed_at"])
        }


    def to_string(self):
        return "Malicious event of type: " + Fore.RED + self.malicious_events_type \
            + Fore.WHITE \
            +   " is detected ! \n" \
            + "The repository named: " + self.data["full_name"] \
            + "\npushed by \n\t" + self.data["pusher"]["name"] \
            + "\n\t" + self.data["pusher"]["email"] \
            + "\n at: " + str(self.data["pushed_at"])

class HackerTeam(MaliciousEvents):
    def __init__(self, notify, data):
        super().__init__(notify)
        self.malicious_events_type = "\'New Team with name begining by \'Hacker\' was added\'"
        self.data = {
            "sender" : data["sender"]["login"],
            "team_name" : data["team"]["name"]
        }


    def to_string(self):
        return "Malicious event of type: \n\t" + Fore.RED + self.malicious_events_type \
            + Fore.WHITE \
            +   " is detected ! \n" \
            + "New team :\t" + self.data["team_name"] \
            + "\nwas added by \t" + self.data["sender"]


def create_repository_deleted_event(notify_function, data):
    return RepositoryDeletedEvent(notify_function, data)


def create_pushing_code_event(notify_function, data):
    return PushingCode(notify_function, data)


def create_hacker_team_event(notify_function, data):
    return HackerTeam(notify_function, data)


def event_factory(event_type, notify_function, data):
    event_creators = {
        "RepositoryDeletedEvent": create_repository_deleted_event,
        "PushingCode": create_pushing_code_event,
        "HackerTeam": create_hacker_team_event,
    }
    creator_func = event_creators.get(event_type)
    if creator_func:
        return creator_func(notify_function, data)
    else:
        raise ValueError(f"Invalid event_type: {event_type}")

