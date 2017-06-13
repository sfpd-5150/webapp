from flask import Flask, render_template
from foo.getdata import get_incidents, get_districts, get_incident_by_id, \
    get_months, get_hoods
from urllib.parse import unquote


app = Flask(__name__)

@app.route("/hello")
def hello():
    return 'hello world'

@app.route("/")
def homepage():
    incidents = get_incidents()
    return render_template("index.html",
                incidents=incidents,
                districts=get_districts(incidents),
                hoods=get_hoods(incidents)
            )


@app.route("/year/<year>")
def yearpage(year):
    incidents = [i for i in get_incidents() if i['year'] == year]
    monthcount = get_months(incidents)
    counts_per_month = [y for x, y in monthcount]


    return render_template("yearpage.html", incidents=incidents, year=year, month_count=monthcount,
            district_count=get_districts(incidents), stuff=counts_per_month
        )


@app.route("/neighborhoods/<name>")
def hoodpage(name):
    nname = unquote(name)
    incidents = [i for i in get_incidents() if i['neighborhood'] == nname]
    return render_template("hood_page.html", incidents=incidents, neighborhood=nname)


@app.route("/pd/<pname>")
def precinctpage(pname):
    pname = pname.upper()
    incidents = [i for i in get_incidents() if i['PdDistrict'] == pname]
    return render_template("pdpage.html", incidents=incidents, district_name=pname)


@app.route("/incidents/<id>")
def incidentpage(id):
    return render_template("incidentpage.html", incident=get_incident_by_id(id))





if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
