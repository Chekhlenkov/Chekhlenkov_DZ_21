class BaseError(Exception):
    message = "Неожиданная ошибка"


class RequestError(BaseError):
    message = "Произошла ошибка обработки заказа"


class CourierError(BaseError):
    message = "Произошла ошибка при доставке"


class NotEnoughSpace(CourierError):
    message = "Недостаточно места на складе"


class NotEnoughProduct(CourierError):
    message = "Недостаточно места на складе"


class TooManyDifferentProducts(CourierError):
    message = "Слишком много разных товаров"


class InvalidRequest(RequestError):
    message = "Неправильный запрос. Попробуйте снова"

class InvalidStorageName(RequestError):
    message = 'Выбран несуществующий склад'

