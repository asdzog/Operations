from utils import read_operations, sort_history, encode_in_account,\
    encode_out_account, print_operation
DATA = "operations.json"
OPERATIONS_AMOUNT = 5


def main():
    history = read_operations(DATA)
    history = sort_history(history, OPERATIONS_AMOUNT)
    for action in history:
        print(print_operation(action), '\n')


if __name__ == "__main__":
    main()
