from werkzeug.exceptions import abort
from flask import render_template
from flask import Blueprint
from Templating_with_Jinja2.jinja_app.jinja_app1.product.models import PRODUCTS

products_bp = Blueprint('product', __name__)

@products_bp.route('/')
@products_bp.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)

@products_bp.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)

    else:
        return render_template('product.html',product= product)

@products_bp.context_processor
def some_processor():
    def full_name(product):
        return '{0} / {1}'.format(product['category'],
          product['name'])
    return {'full_name': full_name}