from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud CI/CD Pipeline is Working!"

@app.route("/version")
def version():
    return "Version 1 - Jenkins + Docker + AWS"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
