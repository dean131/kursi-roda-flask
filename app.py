from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! test cuyyy"


if __name__ == "__main__":
    # Bind to 0.0.0.0 to allow access from outside the container
    app.run(host="0.0.0.0", port=5000, debug=True)
