from os.path import join
import csv
from collections import Counter

DATA_DIR = join('static', 'data')
INCIDENTS_FNAME = join(DATA_DIR, 'incidents.csv')


def get_incidents():
    with open(INCIDENTS_FNAME) as f:
        data = list(csv.DictReader(f))
    return data


def get_districts():
    names = []
    for i in get_incidents():
        names.append(i['PdDistrict'])

    return sorted(Counter(names).items())
