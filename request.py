from typing import Dict
from abstract_storage import AbstractStorage
from exceptions import InvalidRequest, InvalidStorageName

class Request:
    def __init__(self, request: str, storeges: Dict[str, AbstractStorage]):
        splitted_request = request.lower().split(' ')
        if len(splitted_request) !=7:
            raise InvalidRequest

        self.amount = int(splitted_request[1])
        self.product = splitted_request[2]
        self.departure = splitted_request[4]
        self.destination = splitted_request[6]

        if self.departure not in storeges or self.destination not in storeges:
            raise InvalidStorageName