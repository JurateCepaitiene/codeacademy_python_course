from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def user():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def user(name):
    return f"Labas, {name}"

if __name__ == "__main__":
    app.run()


