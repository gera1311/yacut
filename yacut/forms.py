from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import (
    LENGTH_ERROR_MESSAGE,
    MAX_LENGTH_SHORT_ID,
    REGEX_ERROR_MESSAGE,
    REGEX_SHORT_ID,
    REQUIRED_MESSAGE,
    URL_FORM_ERROR_MESSAGE,
)


class URLForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message=REQUIRED_MESSAGE),
                    URL(message=URL_FORM_ERROR_MESSAGE)],
    )
    custom_link_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(max=MAX_LENGTH_SHORT_ID,
                   message=LENGTH_ERROR_MESSAGE),
            Regexp(
                REGEX_SHORT_ID,
                message=REGEX_ERROR_MESSAGE
            )
        ]
    )
    submit = SubmitField('Создать')
