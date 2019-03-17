from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)

from amazon.api import AmazonAPI
from collections import Counter

amazon = AmazonAPI('AKIAIDMLCQFWH64BE5KA','vNpc7x047m9ez18Zfw/90/s6jVj6okixTAr/3QNt','beyourshelves-20') # Inits API

bp = Blueprint('keyword', __name__)

# Default Search Option
@bp.route('/', methods=('GET','POST'))
def searchKW():
    if request.method == 'POST':
        keywords = request.form['search']

        # Gets first page results for top amazon products
        products = amazon.search_n(50,Keywords=keywords, SearchIndex='All')

        getFrequency(products)

        #return render_template('search/output.html', kw=keywords, products=products)

    return render_template('index.html')

def getFrequency(myList):
    bigString = ""

    for product in myList:
        bigString = bigString + str(product)

    result = Counter(bigString.split()).most_common()
    print(result)