import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    return data



def create_graph_data():
    pass

