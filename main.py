"""
Demo app for Prometheus basics.

Concept: a "Jokes" app inspired by #x-blagues (Sapient France's Slack channel)
"""

import json
import uuid


from flask import Flask, request, make_response
from prometheus_client import Counter, Gauge
from prometheus_flask_exporter import PrometheusMetrics


# Initialization
app = Flask(__name__)
metrics = PrometheusMetrics(app)


def gen_new_uuid():
    """Simple helper to generate jokes IDs"""
    return str(uuid.uuid4())[:8]


def api_response_from_dict(content_dict=None):
    """Simple helper to make it easier to return API responses in JSON"""
    if content_dict:
        response = make_response(json.dumps(content_dict))
    else:
        response = make_response()
    response.headers['Content-Type'] = 'application/json'
    return response


# Static information as metric
metrics.info('xblagues_info', 'Application info', version='1.0.0')

# "Business" metrics
number_jokes_counter = Counter(
    name            = 'xblagues_number_jokes',
    documentation   = 'Number of jokes'
)
number_reactions_counter = Counter(
    name            = 'xblagues_number_reactions',
    documentation   = 'Number of reactions',
    labelnames      = ['joke_id']
)
number_channel_members_gauge = Gauge(
    name            = 'xblagues_number_channel_members',
    documentation   = 'Number of members in the channel'
)

# Get some base jokes to work on
jokes = [{'id': gen_new_uuid(), 'content': 'This is a joke', 'reactions': 0},
         {'id': gen_new_uuid(), 'content': 'This is a second joke', 'reactions': 0}]
number_jokes_counter.inc()
number_jokes_counter.inc()

channel_members = [{'id': gen_new_uuid(), 'name': 'Horgix'},
                   {'id': gen_new_uuid(), 'name': 'Frédéric'}]
number_channel_members_gauge.inc()
number_channel_members_gauge.inc()


@app.route('/')
def main():
    pass  # requests tracked by default


@app.route('/jokes')
def get_jokes():
    return api_response_from_dict(jokes)


@app.route('/add_joke')
def add_joke():
    joke = request.args.get('joke')
    new_joke = {"id": gen_new_uuid(), "content": joke, "reactions": 0}
    jokes.append(new_joke)

    number_jokes_counter.inc()

    return api_response_from_dict(new_joke)


@app.route('/add_reaction')
def add_reaction_to_joke():
    joke_id = request.args.get('joke_id')

    jokes_dict = {joke['id']: joke for joke in jokes}
    if "id" not in jokes_dict:
        return api_response_from_dict({"Failed to find joke"})

    jokes_dict[joke_id]['reactions'] += 1

    number_reactions_counter.labels(joke_id).inc()

    updated_joke = jokes_dict[joke_id]

    return api_response_from_dict(updated_joke)


@app.route('/members')
def get_members():
    return api_response_from_dict(channel_members)


@app.route('/add_member')
def add_member():
    member = request.args.get('member')
    new_member = {"id": gen_new_uuid(), "name": member}
    channel_members.append(new_member)

    number_channel_members_gauge.inc()

    return api_response_from_dict(new_member)


@app.route('/remove_member')
def remove_member():
    member_id = request.args.get('member_id')

    member = None
    for m in channel_members:
        if m['id'] == member_id:
            member = m

    member_index = channel_members.index(member)
    channel_members.pop(member_index)

    number_channel_members_gauge.dec()

    return api_response_from_dict()


@app.route('/skip')
@metrics.do_not_track()
def skip():
    pass  # default metrics are not collected


@app.route('/<item_type>')
@metrics.do_not_track()
@metrics.counter('invocation_by_type', 'Number of invocations by type',
                 labels={'item_type': lambda: request.view_args['type']})
def by_type(item_type):
    pass  # only the counter is collected, not the default metrics


@app.route('/long-running')
@metrics.gauge('in_progress', 'Long running requests in progress')
def long_running():
    pass


@app.route('/status/<int:status>')
@metrics.do_not_track()
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def echo_status(status):
    return 'Status: %s' % status, status


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
