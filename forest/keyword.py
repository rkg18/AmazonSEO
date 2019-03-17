from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)

from amazon.api import AmazonAPI
from collections import Counter

NUMBER_OF_PRODUCTS_SEARCH = 10 # CONSTANT VALUE, 10-Products = 1-Page Results

amazon = AmazonAPI('AKIAIDMLCQFWH64BE5KA','vNpc7x047m9ez18Zfw/90/s6jVj6okixTAr/3QNt','beyourshelves-20') # Inits API

bp = Blueprint('keyword', __name__)

# Default Search Option
@bp.route('/', methods=('GET','POST'))
def searchKW():
    if request.method == 'POST':
        keywords = request.form['search']

        # Gets page 1-3 results for products
        products = amazon.search_n(NUMBER_OF_PRODUCTS_SEARCH,Keywords=keywords, SearchIndex='All')

        # Counts Frequency
        keywordFrequencyList = getFrequency(products)

        # Removes unneccessary keywords
        keywordFrequencyList = removeListOfKeywords(keywordFrequencyList)

        # prints
        printList(keywordFrequencyList)

        #return render_template('search/output.html', kw=keywords, products=products)

    return render_template('index.html')

# Counts frequencies of words
def getFrequency(myList):
    bigString = ""

    for product in myList:
        bigString = bigString + str(product)

    result = Counter(bigString.split()).most_common()

    # Returns a 'List' object of all frequencies of element
    return result

# removes individual keyword
def removeKeyword(listItem, word):
    listItem = [t for t in listItem if t[0] != word] 
    return listItem

# Removes multiple keywords
def removeListOfKeywords(keywordFrequencyList):
    keywordFrequencyList = removeKeyword(keywordFrequencyList,'with')
    keywordFrequencyList = removeKeyword(keywordFrequencyList,'for')
    keywordFrequencyList = removeKeyword(keywordFrequencyList,'and')
    keywordFrequencyList = removeKeyword(keywordFrequencyList,'&')
    keywordFrequencyList = removeKeyword(keywordFrequencyList,'to')
    keywordFrequencyList = removeKeyword(keywordFrequencyList,'-')

    return keywordFrequencyList

# Prints a list item
def printList(listObject):
    for i in listObject:
        print(i)