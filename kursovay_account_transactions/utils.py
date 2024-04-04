import json
from datetime import datetime
def loading_file(fail_name):
    """"""
    with open(fail_name, "r") as load_file:
        return json.load(load_file)


def filter_list(load_file):
    """"""
    json_adjective = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', load_file))
    return json_adjective


def sorts_date(json_adjective):
    """"""
    json_sort = sorted(json_adjective,key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return json_sort


def changes_date_format(date):
    """"""
    obj_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(obj_date, '%d.%m.%Y')


def get_hide_num(num):
    """"""
    req = num.split()
    if req[0] == "Счет":
        return 'Счет **' + num[-4:]
    else:
        card_name = " ".join(req[:-1])
        return card_name + ' ' + req[-1][:4] + ' ' + req[-1][4:6] + '** **** ' + req[-1][-4:]


def get_format_summa(cash):
    """Функция формирует сумму в соответствии с фильтрами"""
    return f'{cash["operationAmount"]["amount"]} {cash["operationAmount"]["currency"]["name"]}'


def get_main(num_operations=5):
    """Функция выводит операцию в нужном формате"""
    sorting = sorts_date(filter_list(loading_file("operations.json")))
    for operation in sorting:
        if num_operations == 0:
            break
        print(changes_date_format(operation["date"]), operation["description"])
        if operation["description"] != "Открытие вклада":
            print(get_hide_num(operation["from"]) + " -> ", end="")
        print(get_hide_num(operation["to"]))
        print(get_format_summa(operation), "\n")
        num_operations -= 1











    

