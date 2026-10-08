import collections
import collections.abc
from flask import Flask

# Compatibility fix for nose on Python 3.10+
if not hasattr(collections, "Callable"):
    collections.Callable = collections.abc.Callable

app = Flask(__name__)


@app.route("/")
def home():
    return "SERVICERUNNING"


@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
