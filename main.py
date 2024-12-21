from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! The Digital Burn Book is coming soon...</p>"

if __name__ == "__main__":
    app.run(debug=True)