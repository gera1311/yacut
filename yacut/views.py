from flask import abort, flash, redirect, render_template
from http import HTTPStatus

from . import app
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def generate_short_link():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    try:
        return render_template(
            'index.html',
            form=form,
            shortened_url=URLMap.create(
                form.original_link.data,
                form.custom_id.data or None,
                skip_validation=True
            ).get_short_url()
        )
    except (ValueError, RuntimeError) as e:
        flash(str(e))

    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    url_map = URLMap.get(short)
    if url_map is None:
        abort(HTTPStatus.NOT_FOUND)
    return redirect(url_map.original)
