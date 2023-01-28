from shop import Shop
from store import Store
from exceptions import RequestError, CourierError
from request import Request
from courier import Courier


store = Store(items={})
shop = Shop(items={})

store.items = {
    "печенька": 25,
    "собачка": 25,
    "елка": 25,
    "пончик": 3,
    "зонт": 5,
    "ноутбук": 1,
}

shop.items = {
    "печенька": 2,
    "собачка": 2,
    "елка": 2,
    "пончик": 2,
    "зонт": 1,
}

storeges = {
    'магазин': shop,
    'склад': store,
}

def main():
    print('\nДобрый день\n')

    while True:
        for storege_name in storeges:
            print(f'Сейчас в {storege_name}:\n {storeges[storege_name].items}')

        user_input = input(
            'Введите запрос в формате "Доставить 3 печенька из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_input, storeges=storeges)
        except RequestError as error:
            print(error.message)
            continue

        courier = Courier(
            request=request,
            storeges=storeges,
        )
        try:
            courier.move()
        except CourierError as error:
            print(error.message)
            courier.cancel()



if __name__=='__main__':
    main()
