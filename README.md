

<h1>Malicious Events Detection and Notification System</h1>

<h2>Overview</h2>

<p>This project implements a Flask-based webhook server that detects and notifies about potentially malicious events occurring on repositories.  The system monitors and flags the following suspicious behaviors:</p>
<ol>
    <li><strong>Pushing code between 14:00-16:00</strong>: This could indicate unauthorized or suspicious activity during non-standard working hours.</li>
    <li><strong>Creating a team with the prefix "hacker"</strong>: Such team names might suggest malicious intent or an attempt to gain unauthorized access.</li>
    <li><strong>Creating a repository and deleting it in less than 10 minutes</strong>: This behavior can be indicative of a user trying to hide their tracks after performing a potentially malicious action.</li>
</ol>
<p>It includes modules for event detection (<code>events.py</code>), event checking (<code>check_malicious.py</code>), notification (<code>notify.py</code>), and the server itself (<code>server.py</code>).</p>

<h2>Components</h2>

<ol>
    <li><code>server.py</code></li>
    <p>This is the Flask application serving as a webhook endpoint. It listens for POST requests and checks incoming JSON payloads for malicious events using <code>CheckMaliciousEventTable</code>. Detected events are processed and notifications are sent using the <code>event_factory</code>.</p>
    <li><code>events.py</code></li>
    <p>Defines classes for different types of malicious events (<code>MaliciousEvents</code>). Each event class handles the creation of event-specific notifications (<code>Notify</code>) and formats the event data into human-readable strings (<code>to_string</code>).</p>
    <li><code>notify.py</code></li>
    <p>Provides a simple notification function <code>notify_print</code> using ANSI color codes (via <code>colorama</code>) to print notifications to the console.</p>
    <li><code>check_malicious.py</code></li>
    <p>Contains functions (<code>IsPushedEvent</code>, <code>IsDeletedAfter10Min</code>, <code>IsAddedHackerTeam</code>) used by <code>server.py</code> to check if incoming events meet criteria for being malicious. These functions return <code>True</code> or <code>False</code> based on specific conditions parsed from JSON payloads.</p>
</ol>

<h2>Usage</h2>

<h3>Setup</h3>

<ol>
    <li>Ensure Python 3.x, pip, npm are installed.</li>
    <li>Install dependencies:</li>
    <pre><code>pip install Flask colorama python-dateutil</code></pre>
    <pre><code>npm install --global smee-client</code></pre>
    <li>Go to https://smee.io/ and save YOUR_URL_KEY</li>
    <li>Follow the titorial for add webhook from https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks</li>
</ol>


<h3>Running the Server</h3>

<p>Run the Flask server:</p>

<pre><code>python server.py
</code></pre>

<p>The server will start listening on <code>http://localhost:5000/</code>.</p>
<p>In another terminal, enter the smee command:</p>
<pre><code> npx smee -u https://smee.io/YOUR_URL_KEY -p 5000</code></pre>
<h2>Testing</h2>

<p>Send POST requests with JSON payloads to <code>http://localhost:5000/</code> to trigger event detection and notification. Below are examples for testing the three types of suspicious behaviors:</p>

<h3>1. Pushing Code Between 14:00-16:00</h3>
<p>To simulate pushing code during suspicious hours, use the following Git commands:</p>
<pre><code>git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/AWS-Amazon-AZ/ML-models.git
git push -u origin master
</code></pre>
<p>Ensure the push occurs between 14:00 and 16:00 to trigger the detection.</p>

<h3>2. Creating a Team with the Prefix "hacker"</h3>
<p>To test for creating a team with the prefix "hacker", manually add a team on GitHub:</p>
<ol>
    <li>Navigate to your repository on GitHub.</li>
    <li>Go to <strong>Settings</strong> &gt; <strong>Manage access</strong> &gt; <strong>Teams</strong>.</li>
    <li>Create a new team with a name starting with "hacker", such as "hacker_team".</li>
</ol>

<h3>3. Creating a Repository and Deleting It in Less Than 10 Minutes</h3>
<p>To simulate creating and deleting a repository quickly, manually perform the following steps on GitHub:</p>
<ol>
    <li>Create a new repository.</li>
    <li>Wait for less than 10 minutes.</li>
    <li>Delete the repository.</li>
</ol>

<p>These actions will send the appropriate events to the Flask server, simulating the detection of suspicious behaviors and triggering the corresponding notifications.</p>


<h3>Extending Functionality</h3>

<p>To add new malicious event types:</p>

<ol>
    <li>Define a new function in <code>check_malicious.py</code> that returns <code>True</code> if the event matches certain criteria.</li>
    <li>Update <code>CheckMaliciousEventTable</code> in <code>events.py</code> to include the new event type and corresponding function.</li>
    <li>Create a new class in <code>events.py</code> inheriting from <code>MaliciousEvents</code> to handle the new event type and its notification format.</li>
</ol>

<h2>Dependencies</h2>

<ul>
    <li>Flask: Web framework for handling HTTP requests.</li>
    <li>Colorama: Library for colored terminal text output.</li>
    <li>python-dateutil: Provides extensions to the standard datetime module.</li>
</ul>

<h2>Contributing</h2>

<p>Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>

