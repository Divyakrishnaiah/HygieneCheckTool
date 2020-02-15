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

    v = {"result" : commonelements(inc,exc)}
    return json.dumps(v)

def commonelements(inc,exc):
    commonItems = []
    inc = clearNot(inc)
    exc = clearNot(exc)

    incwords = []
    excwords = []
    for i in inc:
        i=i.strip()
        if 'AttributesContain' in i:
            ind = i.index(':')
            temp = i[ind+1:len(i)-1]
            temp = temp.split('|')
            incwords = [*incwords, *temp]

    for i in exc:
        i=i.strip()
        if 'AttributesContain' in i:
            ind = i.index(':')
            temp = i[ind+1:len(i)-1]
            temp = temp.split('|')
            excwords = [*excwords, *temp]

    for i in incwords:
        for j in excwords:
            if i.casefold() in (j.casefold()).replace(' ','.'):
                commonItems.append(j)

    return commonItems

def clearNot(syntax):
    notindex =[]
    lines = syntax.splitlines()
    for i in range(0,len(lines)):
        lines[i]=lines[i].strip()
    startIndex = 0
    notFlag = False
    endIndex = 0
    for i in range(0,len(lines)):
        if lines[i]== '{NOT':
            for j in range(i,len(lines)):
                if lines[j] == '}':
                    notindex.append((i,j+1))
                    break

    for i in notindex:
        for j in range(i[0],i[1]):
            lines[j] = ''

    lines = [x for x in lines if x != '']
    return lines

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8970)
