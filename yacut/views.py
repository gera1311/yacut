import string
from random import choices

from flask import flash, redirect, render_template

from . import app, db
from .constants import (
    FLASH_NAME_EXISTS_MESSAGE,
    FLASH_READY_SHORT_LINK,
    LENGTH_RANDOM_SHORT_ID,
)
from .forms import URLForm
from .models import URLMap


def random_short_id(length=LENGTH_RANDOM_SHORT_ID):
    characters = string.ascii_letters + string.digits
    short_link = ''.join(choices(characters, k=length))
    return short_link


@app.route('/', methods=['GET', 'POST'])
def generate_short_link():
    form = URLForm()
    if form.validate_on_submit():
        custom_link_id = form.custom_link_id.data
        original_link = form.original_link.data
        if not custom_link_id:
            custom_link_id = random_short_id()
        if URLMap.query.filter_by(custom_link_id=custom_link_id).first():
            flash(FLASH_NAME_EXISTS_MESSAGE)
            return render_template('urlmap.html', form=form)
        urlmap = URLMap(
            original_link=original_link,
            custom_link_id=custom_link_id
        )
        db.session.add(urlmap)
        db.session.commit()
        flash(f'{FLASH_READY_SHORT_LINK}: '
              f'<a href="http://localhost:5000/{urlmap.custom_link_id}">'
              f'http://localhost:5000/{urlmap.custom_link_id}</a>')
    return render_template('urlmap.html', form=form)


@app.route('/<string:short_id>')
def redirect_to_original_link(short_id):
    url_map = URLMap.query.filter_by(custom_link_id=short_id).first_or_404()
    return redirect(url_map.original_link)
