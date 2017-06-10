from os.path import join
import csv
from collections import Counter
from datetime import datetime

DATA_DIR = join('static', 'data')
INCIDENTS_FNAME = join(DATA_DIR, 'incidents.csv')


def get_incidents():
    data = []
    with open(INCIDENTS_FNAME) as f:
        for row in csv.DictReader(f):
            row['X'] = float(row['X'])
            row['Y'] = float(row['Y'])
            dt = row['Date'] + ' ' + row['Time']
            row['datetime'] = datetime.strptime(dt, '%m/%d/%Y %H:%M')
            data.append(row)

    return data

def get_incident_by_id(id):
    for i in get_incidents():
        if i['IncidntNum'] == id:
            return i



def get_districts(incidents):
    names = []
    for i in incidents:
        names.append(i['PdDistrict'])

    return sorted(Counter(names).items())



def get_months(incidents):
    names = []
    for i in incidents:
        mth = i['datetime'].strftime('%B')
        names.append(mth)

    return Counter(names).items()
