import string
from random import choices

from flask import flash, redirect, render_template, url_for

from . import app, db
from .constants import (
    FIELD_EXISTS_MESSAGE,
    FLASH_READY_SHORT_LINK,
    LENGTH_RANDOM_SHORT_ID,
)
from .forms import URLForm
from .models import URLMap


def random_short_id(length=LENGTH_RANDOM_SHORT_ID):
    characters = string.ascii_letters + string.digits
    while True:
        short_link = ''.join(choices(characters, k=length))
        if not URLMap.query.filter_by(short=short_link).first():
            return short_link


@app.route('/', methods=['GET', 'POST'])
def generate_short_link():
    form = URLForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        original_link = form.original_link.data
        if not custom_id:
            custom_id = random_short_id()
        if URLMap.query.filter_by(short=custom_id).first():
            flash(FIELD_EXISTS_MESSAGE)
            return render_template('urlmap.html', form=form)
        urlmap = URLMap(
            original=original_link,
            short=custom_id
        )
        db.session.add(urlmap)
        db.session.commit()
        short_url = url_for('redirect_to_original_link',
                            short_id=urlmap.short, _external=True)
        flash(f'{FLASH_READY_SHORT_LINK}: '
              f'<a href="{short_url}">{short_url}</a>')
    return render_template('urlmap.html', form=form)


@app.route('/<string:short_id>')
def redirect_to_original_link(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)
