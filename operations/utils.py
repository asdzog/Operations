import json


def read_operations(filename) -> list:
    """
    Reads file with operations history and returns last five ones of them
    """
    with open(filename, 'r', encoding='utf-8') as data:
        operations = json.loads(data.read())
    return operations


def sort_history(operations: list, operations_amount: int) -> list:
    """
    Sorts list of operations by date and status 'EXECUTED' and returns list of needed amount operations
    """
    sorted_operations = sorted(operations, key=lambda x: (x.get('state', 'unknown'), x.get('date')), reverse=True)
    last_operations = [op for op in sorted_operations[:operations_amount * 2] if op][:operations_amount]
    return last_operations


def encode_in_account(operation: dict) -> str:
    """
    Encodes source account number into a required format
    """
    account_in, acc_in_num = operation['to'].split()
    return f'{account_in} **{acc_in_num[-4:]}'


def encode_out_account(operation: dict) -> str:
    """
    Encodes purpose account number into a required format
    """
    source = operation.get('from', 'Вкладчик')
    if source != 'Вкладчик':
        account_out = source.split()
        acc_out_num = account_out[-1]
        account_out[-1] = f'{acc_out_num[:4]} {acc_out_num[4:6]}** **** {acc_out_num[-4:]}'
        source = ' '.join(account_out)
    return source


def print_operation(operation: dict) -> str:
    """
    Returns operation information according to output required format
    """
    oper_date = '.'.join(operation['date'][:operation['date'].index('T')].split('-')[::-1])
    description = operation['description']
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    source = encode_out_account(operation)
    purpose = encode_in_account(operation)
    return f'{oper_date} {description}\n{source} -> {purpose}\n{amount} {currency}'
