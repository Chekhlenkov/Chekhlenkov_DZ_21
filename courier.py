from request import Request
from typing import Dict
from abstract_storage import AbstractStorage



class Courier:
    def __init__(self, request: Request, storeges: Dict[str, AbstractStorage]):
        self.__request = request

        if self.__request.departure in storeges:
            self.__from = storeges[self.__request.departure]
        if self.__request.destination in storeges:
            self.__to = storeges[self.__request.destination]

    def move(self):
        self.__from.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.departure}')

        self.__to.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}')

    def cancel(self):
        pass
