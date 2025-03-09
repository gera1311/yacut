from flask import jsonify, request

from . import app, db
from .constants import (
    BODY_ERROR_MESSAGE,
    FIELD_EXISTS_MESSAGE,
    ID_ERROR_MESSAGE,
    SHORT_LINK,
    URL,
    URL_ERROR_MESSAGE,
)
from .exceptions import InvalidAPIUsage
from .models import URLMap
from .validators import validate_custom_id
from .views import random_short_id


@app.route('/api/id/', methods=['POST'])
def add_custom_link():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage(BODY_ERROR_MESSAGE)
    if URL not in data:
        raise InvalidAPIUsage(URL_ERROR_MESSAGE)

    custom_id = data.get('custom_id') or random_short_id()
    validate_custom_id(custom_id)
    if URLMap.query.filter_by(short=custom_id).first():
        raise InvalidAPIUsage(FIELD_EXISTS_MESSAGE)

    urlmap = URLMap(
        original=data[URL],
        short=custom_id
    )
    db.session.add(urlmap)
    db.session.commit()
    return jsonify({
        URL: urlmap.original,
        SHORT_LINK: request.host_url + custom_id
    }), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_link(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage(ID_ERROR_MESSAGE, 404)
    return jsonify({URL: urlmap.original}), 200
