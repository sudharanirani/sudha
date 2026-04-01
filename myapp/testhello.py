from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello World AI testing new phase"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50010, debug=True)
