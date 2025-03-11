import string

LENGTH_RANDOM_SHORT = 6
MAX_LENGTH_SHORT = 16
MAX_LENGTH_ORIGINAL = 2000
MAX_ATTEMPTS = 100
ALLOWED_CHARS = (f'{string.ascii_uppercase}'
                 f'{string.ascii_lowercase}'
                 f'{string.digits}')
REGEX_SHORT = rf'^[{ALLOWED_CHARS}]*$'

VIEW_REDIRECT = 'redirect_view'
