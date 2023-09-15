import os
import json
from datetime import datetime


def read_operations() -> list:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    operations_file_path = os.path.join(current_dir, "operations.json")

    with open(operations_file_path, 'r', encoding='utf-8') as data:
        operations = json.loads(data.read())
    return operations


def filter_operations(operations):
    """
    Filters operations having status 'EXECUTED'
    """
    last_operations = [op for op in operations if 'state' in op and op['state'] == 'EXECUTED']
    return last_operations


def get_last_operations(operations: list, operations_amount: int) -> list:
    """
    Sorts list of operations by date and status 'EXECUTED' and returns list of needed amount operations
    """
    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=True)
    last_operations = sorted_operations[:operations_amount]
    return last_operations


def encode_in_account(operation: dict) -> str:
    """
    Encodes source account number into a required format
    """
    account_params = operation['to'].split()
    account_in = ' '.join(account_params[:-1])
    acc_in_num = account_params[-1]
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
    oper_date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    description = operation['description']
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    source = encode_out_account(operation)
    purpose = encode_in_account(operation)
    return f'{oper_date} {description}\n{source} -> {purpose}\n{amount} {currency}'
