from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Página del cliente"


if __name__ == "__main__":
    app.run(debug=True)
