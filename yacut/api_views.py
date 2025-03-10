from http import HTTPStatus

from flask import jsonify, request

from . import app
from .constants import (
    BODY_ERROR_MESSAGE,
    ID_ERROR_MESSAGE,
    URL_ERROR_MESSAGE,
)
from .exceptions import InvalidAPIUsage
from .models import URLMap


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
            'short_link': URLMap.create(data['url'],
                                        data.get('custom_id')).get_short_url()
        }), HTTPStatus.CREATED
    except InvalidAPIUsage as e:
        raise e


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_link(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map is None:
        raise InvalidAPIUsage(ID_ERROR_MESSAGE, HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK
