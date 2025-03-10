from http import HTTPStatus

from flask import jsonify, request

from . import app
from .exceptions import InvalidAPIUsage
from .models import URLMap

BODY_ERROR_MESSAGE = 'Отсутствует тело запроса'
ID_ERROR_MESSAGE = 'Указанный id не найден'
URL_ERROR_MESSAGE = '"url" является обязательным полем!'
ERROR_GENERATE_SHORT = 'Не удалось сгенерировать уникальный идентификатор'
LENGTH_ERROR_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
SYMBOLS_ERROR_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
FIELD_EXISTS_MESSAGE = 'Предложенный вариант короткой ссылки уже существует.'


@app.route('/api/id/', methods=['POST'])
def add_custom_link():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage(BODY_ERROR_MESSAGE)
    if 'url' not in data:
        raise InvalidAPIUsage(URL_ERROR_MESSAGE)

    try:
        return jsonify({
            'url': data['url'],
            'short_link': URLMap.create(
                original=data['url'],
                short=data.get('custom_id'),
                skip_validation=False
            ).get_short_url(view='redirect_view')
        }), HTTPStatus.CREATED
    except (ValueError, RuntimeError) as e:
        raise InvalidAPIUsage(str(e))


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_link(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map is None:
        raise InvalidAPIUsage(ID_ERROR_MESSAGE, HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK
