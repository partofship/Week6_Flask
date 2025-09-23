from flask import Flask, render_template
# from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    users = [
        {"username": "admin", "realname": "admin"},
        {"username": "honeybadger", "realname": "Samuel"},
        {"username": "hospital", "realname": "Max"},
        {"username": "murder ink", "realname": "Rodney"}
    ]
    return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run(debug=True, port=5023)