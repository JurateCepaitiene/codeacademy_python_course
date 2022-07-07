
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "<h1> Hello world <h1>"

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     vardai = ['Jonas', 'Antanas', 'Petras']
#     return render_template("index.html", sarasas=vardai)

# if __name__ == "__main__":
#     app.run()

# from flask import Flask, request, render_template
# app = Flask(__name__)

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         vardas = request.form['vardas']
#         return render_template("greetings.html", vardas=vardas)
#     else:
#         return render_template("login.html")

# if __name__ == "__main__":
#     app.run()

from query import db, Query, app
from flask import request, render_template

