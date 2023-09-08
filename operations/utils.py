import json
DATA = "operations.json"


def read_last_history():
    with open(DATA, 'r', encoding='utf-8') as data:
        operations = json.loads(data.read())
    return operations
