from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud CI/CD Pipeline - Version 2 is Working!"

@app.route("/version")
def version():
    return "Version 2 - Automatically Deployed by Jenkins!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)