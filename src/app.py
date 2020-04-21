"""Main application definition.

A simple endpoint that returns a response based on the ECHO_MESSAGE
environment variable.
"""

import os

from flask import Flask

from constants import (
    DEFAULT_DEBUG,
    DEFAULT_HOST,
    DEFAULT_MESSAGE,
    DEFAULT_PORT,
    ENV_DEBUG,
    ENV_ECHO_MESSAGE,
    ENV_HOST,
    ENV_PORT,
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    """Return a basic response based on the set ECHO_MESSAGE."""
    message = os.getenv(ENV_ECHO_MESSAGE, DEFAULT_MESSAGE)
    return {"message": message}, 200


if __name__ == "__main__":
    app.run(
        host=os.getenv(ENV_HOST, DEFAULT_HOST),
        port=os.getenv(ENV_PORT, DEFAULT_PORT),
        debug=os.getenv(ENV_DEBUG, DEFAULT_DEBUG),
    )
