import json
from delimeter import Plotter
DATA_FILE_PATH = 'C:\lab\lab_3\data.json'


@Plotter
def get_data():
    with open(DATA_FILE_PATH, 'r') as f:
        data = json.load(f)
    return data