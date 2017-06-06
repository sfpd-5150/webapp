from os.path import join
import csv

DATA_DIR = join('static', 'data')
INCIDENTS_FNAME = join(DATA_DIR, 'incidents.csv')


def get_incidents():
    with open(INCIDENTS_FNAME) as f:
        data = list(csv.DictReader(f))
    return data
