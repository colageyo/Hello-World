from json import dumps
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.eventbrite import get_events as eventbrite_events

APP = Flask(__name__)

def sendSuccess(data):
    return dumps(data)

def sendError(message):
    return dumps({
        '_error' : message
    })

@APP.route('/events/get_all', methods = ['GET'])
def get_all_events():

    events = list(map(lambda e : e.get_json(), eventbrite_events()))

    try:
        
        return sendSuccess({
            "events": events
        })
    except ValueError as e:
        return sendError(e.args)

if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))