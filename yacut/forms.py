from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import (
    MAX_LENGTH_ORIGINAL,
    MAX_LENGTH_SHORT,
    REGEX_SHORT,
)

REQUIRED_MESSAGE = 'Обязательное поле'
URL_FORM_ERROR_MESSAGE = 'Некорректный URL'
REGEX_ERROR_MESSAGE = 'Допустимы только латинские буквы и цифры'
SUBMIT_BUTTON_TEXT = 'Создать'
LENGTH_ERROR_MESSAGE = 'Указано недопустимое имя для короткой ссылки'


class URLForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message=REQUIRED_MESSAGE),
                    Length(max=MAX_LENGTH_ORIGINAL,
                           message=LENGTH_ERROR_MESSAGE),
                    URL(message=URL_FORM_ERROR_MESSAGE)],
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
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
