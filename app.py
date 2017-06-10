from flask import Flask, render_template
from foo.getdata import get_incidents, get_districts, get_months

app = Flask(__name__)

@app.route("/hello")
def hello():
    return 'hello world'

@app.route("/")
def homepage():
    incidents = get_incidents()
    return render_template("index.html", incidents=incidents, districts=get_districts(incidents))


@app.route("/year/<year>")
def yearpage(year):
    incidents = [i for i in get_incidents() if i['year'] == year]
    return render_template("yearpage.html", incidents=incidents, year=year, month_count=get_months(incidents),
            district_count=get_districts(incidents)
        )

@app.route("/pd/<pname>")
def precinctpage(pname):
    pname = pname.upper()
    incidents = [i for i in get_incidents() if i['PdDistrict'] == pname]
    return render_template("pdpage.html", incidents=incidents, district_name=pname)




if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

