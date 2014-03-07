import json


def serialize(data, filename):
    """ dump json representation of python data structures to file """
    data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    f = open(filename, 'w')
    f.write(data)
    f.close()


def deserialize(file):
    """ read data file and marshall json back to python data structures """
    with open(file, 'r') as f:
        data = f.read()
    return json.loads(data)


