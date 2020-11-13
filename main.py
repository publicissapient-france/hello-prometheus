import random
import time

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)


@app.route('/')
def render():
    time.sleep(random.random() * 0.2)
    return 'ok'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
