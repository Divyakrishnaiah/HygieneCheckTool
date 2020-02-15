import os, json
from flask import *

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/commonkeywords")
def commonkeywords():
    return render_template("commonkeywords.html")

@app.route("/compare", methods=['POST'])
def compare():
    inc = request.form['include']
    exc = request.form['exclude']

    v = {"result" : ['str1', 'str2']}
    return json.dumps(v)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8970)
