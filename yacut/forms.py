from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


class URLForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Некорректный URL')],
    )
    custom_link = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(max=16, message='Максимальная длина ссылки 6 символов'),
            Regexp(
                r'^[A-Za-z0-9]*$',
                message='Допустимы только латинские буквы и цифры'
            )
        ]
    )
    submit = SubmitField('Создать')
