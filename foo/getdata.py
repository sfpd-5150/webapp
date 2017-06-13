from os.path import join
import csv
from collections import Counter
from datetime import datetime



DATA_DIR = join('static', 'data')
INCIDENTS_FNAME = join(DATA_DIR, 'incidents_with_hoods.csv')


def get_incidents():
    data = []
    with open(INCIDENTS_FNAME) as f:
        for row in csv.DictReader(f):
            row['longitude'] = float(row['longitude'])
            row['latitude'] = float(row['latitude'])
            if not row['neighborhood']:
                row['neighborhood'] = 'N/A'
            dt = row['date'] + ' ' + row['time']

            row['datetime'] = datetime.strptime(dt, '%m/%d/%Y %H:%M:00')
            data.append(row)



    return data

def get_incident_by_id(id):
    for i in get_incidents():
        if i['incidntnum'] == id:
            return i


def get_districts(incidents):
    names = []
    for i in get_incidents():
        names.append(i['pddistrict'])

    return sorted(Counter(names).items())


def get_hoods(incidents):
    names = []
    for i in get_incidents():
        names.append(i['neighborhood'])

    return sorted(Counter(names).items())


def get_months(incidents):

    names = []
    for i in incidents:
        mth = i['datetime'].strftime('%m')
        names.append(mth)

    return sorted(Counter(names).items())
