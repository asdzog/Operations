from utils import (read_operations, filter_operations, get_last_operations,
                   encode_in_account, encode_out_account, print_operation)
DATA = "operations.json"
OPERATIONS_AMOUNT = 5


def main():
    history = read_operations(DATA)
    filtered_history = filter_operations(history)
    last_history = get_last_operations(filtered_history, OPERATIONS_AMOUNT)
    for action in last_history:
        print(print_operation(action), '\n')


if __name__ == "__main__":
    main()
