from flask import Flask


app = Flask(__name__)


@app.route("/hello")
def index():
    return "hello world Pinku"

@app.route("/")
def home():
    return "This is Home Page"

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)