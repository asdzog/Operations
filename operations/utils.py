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


def print_operation(operation: dict) -> str:
    """
    Returns operation information according to requirement format
    """
    op_date = '.'.join(operation['date'][:operation['date'].index('T')].split('-')[::-1])
    descript = operation['description']
    source = operation.get('from', 'Вкладчик')
    if source != 'Вкладчик':
        account_out = source.split()
        acc_out_num = account_out[-1]
        account_out[-1] = f'{acc_out_num[:4]} {acc_out_num[4:6]}** **** {acc_out_num[-4:]}'
        source = ' '.join(account_out)
    account_in, acc_in_num = operation['to'].split()
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    operation = f'{op_date} {descript}\n{source} -> {account_in} **{acc_in_num[-4:]}\n{amount} {currency}'
    return operation
