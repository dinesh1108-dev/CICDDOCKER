from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route("/about")
def about():
    return "this about page"

if __name__ == "__main__":
    app.run()
