from flask import Blueprint, render_template, url_for

main_bp = Blueprint('main', __name__, url_prefix='/')

@main_bp.route('/')
def index():
    img_prefix = url_for('static', filename='img/')
    return render_template('index.html', img_prefix=img_prefix)

@main_bp.route('/contact')
def contact():
    img_prefix = url_for('static', filename='img/')
    return render_template('contact.html', img_prefix=img_prefix)

@main_bp.route('/publications')
def publications():
    img_prefix = url_for('static', filename='img/')
    return render_template('publications.html', img_prefix=img_prefix)