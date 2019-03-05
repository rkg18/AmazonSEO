from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)

from amazon.api import AmazonAPI

amazon = AmazonAPI('AKIAIDMLCQFWH64BE5KA','vNpc7x047m9ez18Zfw/90/s6jVj6okixTAr/3QNt','beyourshelves-20') # Inits API

bp = Blueprint('keyword', __name__)

# Default Search Option
@bp.route('/', methods=('GET','POST'))
def searchKW():
    if request.method == 'POST':
        keywords = request.form['search']

        # Gets first page results for top amazon products
        products = amazon.search_n(10,Keywords=keywords, SearchIndex='All')

        return render_template('search/output.html', kw=keywords, products=products)

    return render_template('index.html')