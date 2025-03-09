from flask import render_template, jsonify

from . import app
from .constants import (
    INTERNAL_SERVER_ERROR_500,
    PAGE_NOT_FOUND_404,
)
from .exceptions import InvalidAPIUsage


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(PAGE_NOT_FOUND_404)
def page_not_found(error):
    return render_template('404.html'), PAGE_NOT_FOUND_404


@app.errorhandler(INTERNAL_SERVER_ERROR_500)
def internal_server_error(error):
    return render_template('500.html'), INTERNAL_SERVER_ERROR_500
