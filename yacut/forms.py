from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import (
    MAX_LENGTH_ORIGINAL,
    MAX_LENGTH_SHORT,
    REGEX_SHORT,
)

TITLE_ORIGINAL_LINK = 'Длинная ссылка'
TITLE_SHORT = 'Ваш вариант короткой ссылки'
REQUIRED_MESSAGE = 'Обязательное поле'
URL_FORM_ERROR_MESSAGE = 'Некорректный URL'
REGEX_ERROR_MESSAGE = 'Допустимы только латинские буквы и цифры'
SUBMIT_BUTTON_TEXT = 'Создать'
LENGTH_ERROR_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
FIELD_EXISTS_MESSAGE = 'Предложенный вариант короткой ссылки уже существует.'


class URLForm(FlaskForm):
    original_link = StringField(
        TITLE_ORIGINAL_LINK,
        validators=[DataRequired(message=REQUIRED_MESSAGE),
                    Length(max=MAX_LENGTH_ORIGINAL,
                           message=LENGTH_ERROR_MESSAGE),
                    URL(message=URL_FORM_ERROR_MESSAGE)],
    )
    custom_id = StringField(
        TITLE_SHORT,
        validators=[
            Optional(),
            Length(max=MAX_LENGTH_SHORT,
                   message=LENGTH_ERROR_MESSAGE),
            Regexp(
                REGEX_SHORT,
                message=REGEX_ERROR_MESSAGE
            )
        ]
    )
    submit = SubmitField(SUBMIT_BUTTON_TEXT)
