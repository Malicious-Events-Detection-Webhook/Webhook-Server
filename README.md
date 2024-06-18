Malicious Events Detection and Notification System
Overview
This project implements a Flask-based webhook server that detects and notifies about potentially malicious events occurring on repositories. It includes modules for event detection (events.py), event checking (check_malicious.py), notification (notify.py), and the server itself (server.py).

Components
1. server.py
This is the Flask application serving as a webhook endpoint. It listens for POST requests and checks incoming JSON payloads for malicious events using CheckMaliciousEventTable. Detected events are processed and notifications are sent using the event_factory.

2. events.py
Defines classes for different types of malicious events (MaliciousEvents). Each event class handles the creation of event-specific notifications (Notify) and formats the event data into human-readable strings (to_string).

3. notify.py
Provides a simple notification function notify_print using ANSI color codes (via colorama) to print notifications to the console.

4. check_malicious.py
Contains functions (IsPushedEvent, IsDeletedAfter10Min, IsAddedHackerTeam) used by server.py to check if incoming events meet criteria for being malicious. These functions return True or False based on specific conditions parsed from JSON payloads.

Usage
Setup
Ensure Python 3.x and pip are installed.
Install dependencies:
bash
Copy code
pip install Flask colorama python-dateutil
Running the Server
Run the Flask server:

bash
Copy code
python server.py
The server will start listening on http://localhost:5000/.

Testing
Send POST requests with JSON payloads to http://localhost:5000/ to trigger event detection and notification.

Example:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"action": "deleted", "repository": {"full_name": "test/repo", "created_at": "2024-06-19T12:00:00Z", "updated_at": "2024-06-19T12:09:00Z"}}' http://localhost:5000/
Extending Functionality
To add new malicious event types:

Define a new function in check_malicious.py that returns True if the event matches certain criteria.
Update CheckMaliciousEventTable in events.py to include the new event type and corresponding function.
Create a new class in events.py inheriting from MaliciousEvents to handle the new event type and its notification format.
Dependencies
Flask: Web framework for handling HTTP requests.
Colorama: Library for colored terminal text output.
python-dateutil: Provides extensions to the standard datetime module.
Contributing
Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

