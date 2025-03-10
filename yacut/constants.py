import string

# Общие константы
LENGTH_RANDOM_SHORT = 6
MAX_LENGTH_SHORT = 16
MAX_LENGTH_ORIGINAL = 2000
MAX_ATTEMPTS = 100
ALLOWED_CHARS = ''.join([
    string.ascii_uppercase,
    string.ascii_lowercase,
    string.digits,
])
REGEX_SHORT = rf'^[{ALLOWED_CHARS}]*$'

# Сообщения API
BODY_ERROR_MESSAGE = 'Отсутствует тело запроса'
ID_ERROR_MESSAGE = 'Указанный id не найден'
URL_ERROR_MESSAGE = '"url" является обязательным полем!'

# Сообщения валидации форм
REQUIRED_MESSAGE = 'Обязательное поле'
URL_FORM_ERROR_MESSAGE = 'Некорректный URL'
REGEX_ERROR_MESSAGE = 'Допустимы только латинские буквы и цифры'
LENGTH_ERROR_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
SUBMIT_BUTTON_TEXT = 'Создать'

# Сообщения для пользовательского интерфейса
FIELD_EXISTS_MESSAGE = 'Предложенный вариант короткой ссылки уже существует.'
FLASH_NAME_EXISTS_MESSAGE = 'Имя уже занято!'
FLASH_READY_SHORT_LINK = 'Ваша новая ссылка готова:'
ERROR_GENERATE_SHORT = 'Не удалось сгенерировать уникальный идентификатор'
SYMBOLS_ERROR_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
