import re
from datetime import datetime
from http import HTTPStatus
from random import choices
from flask import abort, request

from . import db
from .constants import (
    ALLOWED_CHARS,
    ERROR_GENERATE_SHORT,
    FIELD_EXISTS_MESSAGE,
    LENGTH_ERROR_MESSAGE,
    LENGTH_RANDOM_SHORT,
    MAX_ATTEMPTS,
    MAX_LENGTH_ORIGINAL,
    MAX_LENGTH_SHORT,
    REGEX_SHORT,
    SYMBOLS_ERROR_MESSAGE,
)
from .exceptions import InvalidAPIUsage


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LENGTH_ORIGINAL), nullable=False)
    short = db.Column(db.String(MAX_LENGTH_SHORT), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @staticmethod
    def is_short_unique(short):
        """Проверяет, уникален ли короткий идентификатор."""
        return URLMap.query.filter_by(short=short).first() is None

    @staticmethod
    def get_unique_short():
        """Генерирует уникальный короткий идентификатор."""
        for _ in range(MAX_ATTEMPTS):
            short = ''.join(choices(ALLOWED_CHARS, k=LENGTH_RANDOM_SHORT))
            if URLMap.is_short_unique(short):
                return short
        raise InvalidAPIUsage(ERROR_GENERATE_SHORT)

    @staticmethod
    def create(original, short=None):
        """Создает новое сопоставление URL-адресов."""
        if short is not None:
            if len(short) > MAX_LENGTH_SHORT:
                raise InvalidAPIUsage(LENGTH_ERROR_MESSAGE)
            if not re.match(REGEX_SHORT, short):
                raise InvalidAPIUsage(SYMBOLS_ERROR_MESSAGE)
            if not URLMap.is_short_unique(short):
                raise InvalidAPIUsage(FIELD_EXISTS_MESSAGE)
        else:
            short = URLMap.get_unique_short()

        url_map = URLMap(original=original, short=short)
        try:
            db.session.add(url_map)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(HTTPStatus.INTERNAL_SERVER_ERROR)
        return url_map

    @staticmethod
    def get_by_short(short):
        """Получает объект URLMap по короткому идентификатору."""
        url_map = URLMap.query.filter_by(short=short).first()
        if url_map is None:
            abort(HTTPStatus.NOT_FOUND)
        return url_map

    def get_short_url(self):
        """Возвращает полный URL короткой ссылки."""
        return request.host_url + self.short

    def to_dict(self):
        """Преобразует объект URLMap в словарь."""
        return dict(
            url=self.original,
            short=self.get_short_url()
        )
