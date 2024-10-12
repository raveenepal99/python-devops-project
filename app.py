from flask import Flask
import logging

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    logger.info("Home page accessed")
    return "Hello, DevOps Pipeline! This is a simplified message."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
