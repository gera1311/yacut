from flask import abort, flash, redirect, render_template
from http import HTTPStatus

from . import app
from .forms import URLForm
from .models import URLMap

FIELD_EXISTS_MESSAGE = 'Предложенный вариант короткой ссылки уже существует.'


@app.route('/', methods=['GET', 'POST'])
def generate_short_link():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    try:
        url_map = URLMap.create(
            form.original_link.data,
            form.custom_id.data or None,
            skip_validation=True
        )
        return render_template(
            'index.html',
            form=form,
            shortened_url=url_map.get_short_url(view='redirect_view')
        )
    except Exception:
        flash(FIELD_EXISTS_MESSAGE)

    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    url_map = URLMap.get_short(short)
    if url_map is None:
        abort(HTTPStatus.NOT_FOUND)
    return redirect(url_map.original)
