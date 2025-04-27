# app.py
from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "access.log"

def log_message(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

@app.route('/')
def home():
    return '''
    <h1>Welcome to My Flask App!</h1>
    <p><a href="/your_name">Say Hello</a></p>
    <p><a href="/datetime">Get Current Date and Time</a></p>
    <p><a href="/log">View Log</a></p>
    '''


@app.route('/your_name')
def your_name():
    log_message("/your_name endpoint was accessed")
    return "Hello world from James Godwin!"  # Use my name lol

@app.route('/datetime')
def get_datetime():
    log_message("/datetime endpoint was accessed")
    return f"Current date and time: {datetime.now()}"

@app.route('/log')
def view_log():
    try:
        with open(LOG_FILE, "r") as log:
            log_contents = log.read()
        return Response(log_contents, mimetype='text/plain')
    except FileNotFoundError:
        return "Log file not found.", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001
            )
