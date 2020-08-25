from flask import *
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method=="POST":
        username = request.form['username']
        print(username)
        return render_template('destination.html')
    return render_template('forms.html')

@app.route("/get")
def get():
    username = request.args.get('username')
    print(username)
    return render_template('destination.html')

app.run(debug=True)
