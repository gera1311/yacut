from . import app


@app.route('/api/id/', methods=['POST'])
def generate_short_link():
    ...


@app.route('/api/id/<short_id>/', methods=['GET'])
def redirect_to_original_link(short_id):
    ...
