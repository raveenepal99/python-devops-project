from flask import Flask
import os
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer
import logging

app = Flask(__name__)

# Instrumentation Key from environment variable
instrumentation_key = os.environ.get('APPINSIGHTS_INSTRUMENTATIONKEY')

# Setup logging
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={instrumentation_key}'))

# Setup tracing
middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string=f'InstrumentationKey={instrumentation_key}'),
    sampler=ProbabilitySampler(rate=1.0)
)

@app.route('/')
def home():
    logger.warning('Home page accessed')
    return 'Hello, DevOps Pipeline! This is an updated message.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
