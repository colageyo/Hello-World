import http
import json
import logging
import sys

import flask
from flask_cors import CORS

import src.eventbrite
import src.events_cache
import src.events_filter

DEFAULT_PORT_NUM = 5000

APP = flask.Flask(__name__)
CORS(APP)


def send_success(data):
    return json.dumps(data)


def send_error(message):
    return json.dumps({
        '_error': message
    })

@APP.route('/conditions', methods=['GET'])
def get_current_conditions():
    conditions = src.weather.get_weather_by_city('sydney').get_json()
    try:
        return send_success({
            "conditions": conditions
        })
    except Exception as e:
        return send_error(e.args)

@APP.route('/events/recommended', methods=['POST'])
def get_recommended_events():
    if flask.request.content_type != 'application/json':
        flask.abort(http.HTTPStatus.BAD_REQUEST)

    request_data = flask.request.json

    tags = set()

    try:
        tags = set(request_data['tags'])
    except KeyError:
        logging.error("Failed to retrieve tags from malformed request body.")
        flask.abort(http.HTTPStatus.BAD_REQUEST)
    collected_events = src.events_cache.load_events()
    filtered_events = src.events_filter.filter_events(collected_events, tags)

    try:
        return send_success([event.get_serializable_json() for event in filtered_events])
    except ValueError as e:
        return send_error(e.args)


@APP.route('/events/get_all', methods=['GET'])
def get_all_events():
    events = list(map(lambda event: event.get_json(), src.eventbrite.get_events()))

    try:
        return send_success({
            "events": events
        })
    except ValueError as e:
        return send_error(e.args)


if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PORT_NUM))
