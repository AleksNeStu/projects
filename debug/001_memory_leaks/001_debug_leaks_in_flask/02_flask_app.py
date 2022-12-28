import gc
from flask import Flask
# from helpers import _get_service_metrics, json_response

app = Flask('pycon')

@app.route('/metrics/<service>')
@json_response
def get_service_metrics(service):
    # returns list of metric data points
    data = _get_service_metrics(service)
    gc.collect()
    return data
