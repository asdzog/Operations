import json
DATA = "operations.json"


def read_last_history() -> list:
    """
    Reads file with operations history and returns last five ones of them
    """
    with open(DATA, 'r', encoding='utf-8') as data:
        operations = json.loads(data.read())
    sorted_operations = sorted(operations, key=lambda x: (x.get('state', 'unkwnown'), x.get('date')), reverse=True)
    last_operations = [op for op in sorted_operations[:10] if op][:5]
    return last_operations
