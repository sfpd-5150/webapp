from flask import Flask, render_template
from foo.getdata import get_incidents

app = Flask(__name__)

@app.route("/hello")
def hello():
    return 'hello world'

@app.route("/")
def homepage():
    return render_template("index.html", incidents=get_incidents())


@app.route("/year/<year>")
def yearpage(year):
    incidents = [i for i in get_incidents() if i['year'] == year]
    return render_template("yearpage.html", incidents=incidents, year=year)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

