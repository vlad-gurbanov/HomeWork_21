from entity.courier import Courier
from entity.exeptions import BaseError
from entity.request import Request
from entity.shop import Shop
from entity.store import Store

shop = Shop(
    items={
        "печенька": 3,
        "ноутбук": 10,
        "елка": 1,
        # "собака": 2,
        # "кошка": 1,
    },
)

store = Store(
    items={
        "печенька": 10,
        "ноутбук": 20,
        "компьютер": 1,
    },
)
storages = {
    "магазин": shop,
    "склад": store,
}


def main():
    while True:
        # Вывод содержимого складов
        for storage_name in storages:
            print(f"В {storage_name} хранится: {storages[storage_name].get_items()}")

        # Запрос строки у пользователя
        user_input = input(
            'Введите слово в формате "Доставить 3 печенька из склад в магазин".\n'
            'Введите "stop" или "стоп", чтоб продолжить:\n'
        )
        if user_input in ('stop', 'стоп'):
            break

        # Обработка строки, проверка на ошибки, определение товара, количества, точки отправления и назначения
        try:
            request = Request(request_str=user_input, storages=storages)
            # destination = storages[request.destination]
            # departure = storages[request.departure]
        except BaseError as error:
            print(error.message)
            continue

        # Доставка товара
        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except BaseError as error:
            courier.cancel()
            print(error.message)


if __name__ == '__main__':
    main()
