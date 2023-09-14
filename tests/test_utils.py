from operations.utils import (read_operations, filter_operations, get_last_operations,
                   encode_in_account, encode_out_account, print_operation)


# def test_read_operations():
#     operations = read_operations()
#     assert type(operations) == list


def test_filter_operations():
    operations = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
                  {"id": 431131847, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
                  {"id": 692008409, "state": "CANCELED", "date": "2019-02-14T17:38:09.910336"}]

    sorted_operations = filter_operations(operations)

    assert len(sorted_operations) == 2
    assert sorted_operations[0]['id'] == 441945886
    assert sorted_operations[1]['id'] == 431131847


def test_get_last_operations():
    operations = [{"id": 854048120, "state": "EXECUTED", "date": "2019-03-29T10:57:20.635567"},
                  {"id": 269462132, "state": "EXECUTED", "date": "2018-08-14T05:42:30.104666"},
                  {"id": 431131847, "state": "EXECUTED", "date": "2018-05-05T01:38:56.538074"},
                  {"id": 15948212, "state": "EXECUTED", "date": "2018-12-23T11:47:52.403285"},
                  {"id": 114832369, "state": "EXECUTED", "date": "2019-12-07T06:17:14.634890"}]
    assert get_last_operations(operations, 2) == [
        {"id": 114832369, "state": "EXECUTED", "date": "2019-12-07T06:17:14.634890"},
        {"id": 854048120, "state": "EXECUTED", "date": "2019-03-29T10:57:20.635567"}
                  ]
    assert len(get_last_operations(operations, 4)) == 4


def test_encode_in_account():
    operations = [{"description": "Перевод с карты на карту",
                   "from": "МИР 8665240839126074",
                   "to": "Maestro 3000704277834087"},
                  {"description": "Перевод организации",
                   "from": "Visa Classic 2842878893689012",
                   "to": "Счет 35158586384610753655"},
                  {"description": "Открытие вклада",
                   "to": "Счет 90417871337969064865"}]
    assert encode_in_account(operations[0]) == 'Maestro **4087'
    assert encode_in_account(operations[1]) == 'Счет **3655'
    assert encode_in_account(operations[2]) == 'Счет **4865'


def test_encode_out_account():
    operations = [{"description": "Перевод с карты на карту",
                   "from": "МИР 8665240839126074",
                   "to": "Maestro 3000704277834087"},
                  {"description": "Перевод организации",
                   "from": "Visa Classic 2842878893689012",
                   "to": "Счет 35158586384610753655"},
                  {"description": "Открытие вклада",
                   "to": "Счет 90417871337969064865"}]
    assert encode_out_account(operations[0]) == 'МИР 8665 24** **** 6074'
    assert encode_out_account(operations[1]) == 'Visa Classic 2842 87** **** 9012'
    assert encode_out_account(operations[2]) == 'Вкладчик'

def test_print_operation():
    operations = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                   "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Перевод организации", "from": "Maestro 1596837868705199",
                   "to": "Счет 64686473678894779589"},
                  {"id": 587085106, "state": "EXECUTED", "date": "2018-03-23T10:45:06.972075",
                   "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Открытие вклада", "to": "Счет 41421565395219882431"},
                  {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
                   "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                   "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
                   "to": "Visa Platinum 8990922113665229"}]

    assert print_operation(operations[0]) == (f'26.08.2019 Перевод организации\n'
                                              f'Maestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.')
    assert print_operation(operations[1]) == (f'23.03.2018 Открытие вклада\n'
                                              f'Вкладчик -> Счет **2431\n48223.05 руб.')
    assert print_operation(operations[2]) == (f'19.08.2018 Перевод с карты на карту\n'
                                              f'Visa Classic 6831 98** **** 7658 -> Visa Platinum **5229'
                                              f'\n56883.54 USD')
