import re

from .constants import (
    LENGTH_ERROR_MESSAGE,
    SYMBOLS_ERROR_MESSAGE,
)
from .exceptions import InvalidAPIUsage


def validate_custom_id(custom_short_link_id):
    """Валидация custom_id: длина и допустимые символы."""
    if len(custom_short_link_id) > 16:
        raise InvalidAPIUsage(LENGTH_ERROR_MESSAGE)
    if not re.match(r'^[A-Za-z0-9]*$', custom_short_link_id):
        raise InvalidAPIUsage(SYMBOLS_ERROR_MESSAGE)
