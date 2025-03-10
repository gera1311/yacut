from http import HTTPStatus

from flask import render_template, jsonify
from sqlalchemy.exc import SQLAlchemyError

from . import app, db
from .exceptions import InvalidAPIUsage

DB_ERROR_MESSAGE = 'Произошла внутренняя ошибка базы данных.'


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR


@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy_error(error):
    db.session.rollback()
    return jsonify({
        "message": DB_ERROR_MESSAGE,
        "error": str(error)
    }), HTTPStatus.INTERNAL_SERVER_ERROR
