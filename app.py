from flask import Flask
import os
import logging

app = Flask(__name__)

# Instrumentation Key from environment variable
import logging
from flask import Flask
import os

app = Flask(__name__)

# Set up logging
instrumentation_key = os.environ.get('APPLICATIONINSIGHTS_CONNECTION_STRING')
if instrumentation_key:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Adjust log level as needed

    # Assuming the key is set, it will send logs to Application Insights
    logger.info("Application Insights logging is configured.")
else:
    print("No Application Insights connection string found.")

@app.route('/')
def home():
    logger.info('Home page accessed')
    return 'Hello, DevOps Pipeline! This is an updated message.'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)

