from flask import jsonify, request

from . import app
from .constants import (
    BODY_ERROR_MESSAGE,
    CREATED_201,
    ID_ERROR_MESSAGE,
    OK_200,
    PAGE_NOT_FOUND_404,
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
        }), CREATED_201
    except InvalidAPIUsage as e:
        raise e


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_link(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map is None:
        raise InvalidAPIUsage(ID_ERROR_MESSAGE, PAGE_NOT_FOUND_404)
    return jsonify({'url': url_map.original}), OK_200
