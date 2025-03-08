import string
from random import choices

from flask import redirect, render_template, flash

from . import app, db
from .forms import URLForm
from .models import URLMap

LENGTH = 6
FLASH_READY_SHORT_LINK = 'Короткая ссылка успешно создана'


def random_short_id(length=LENGTH):
    if length < 1:
        raise ValueError('Длина короткой ссылки должна быть больше 0')
    characters = string.ascii_letters + string.digits
    short_link = ''.join(choices(characters, k=length))
    return short_link


@app.route('/', methods=['GET', 'POST'])
def generate_short_link():
    form = URLForm()
    if form.validate_on_submit():
        custom_link = form.custom_link.data
        original_link = form.original_link.data
        if URLMap.query.filter_by(custom_link=custom_link).first():
            flash('Имя уже занято!')
            return render_template('urlmap.html', form=form)
        if custom_link is None:
            custom_link = random_short_id()
        urlmap = URLMap(
            original_link=original_link,
            custom_link=custom_link
        )
        db.session.add(urlmap)
        db.session.commit()
        flash(f'{FLASH_READY_SHORT_LINK}: '
              f'<a href="http://localhost:5000/{urlmap.custom_link}">'
              f'http://localhost:5000/{urlmap.custom_link}</a>')
    return render_template('urlmap.html', form=form)


@app.route('/<string:short>')
def redirect_to_original_link(short):
    url_map = URLMap.query.filter_by(custom_link=short).first_or_404()
    return redirect(url_map.original_link)
