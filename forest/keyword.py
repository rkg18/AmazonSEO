from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)

from collections import Counter
from forest.info import *
from forest.price import getProductPrice, getPriceResultsList, getPriceRanges
from forest.images import downloadProductImages, getProductUrl

import random

NUMBER_OF_PRODUCTS_SEARCH = 30 # CONSTANT VALUE, 10-Products = 1-Page Results

bp = Blueprint('keyword', __name__)

# Default Search Option
@bp.route('/', methods=('GET','POST'))
def searchKW():
    if request.method == 'POST':
        keywords = request.form['search']

        # Gets page 1-3 results for products
        products = amazon.search_n(NUMBER_OF_PRODUCTS_SEARCH,Keywords=keywords, SearchIndex='All')

        # gets images to server
        #urlList = downloadProductImages(products)
        productImageUrls = getProductUrl(products)

        # calculates product pricing
        listOfProductPrices = getProductPrice(products)
        minMaxAvg = getPriceResultsList(listOfProductPrices)
        priceTuple = getPriceRanges(listOfProductPrices, minMaxAvg[1])
        priceColors = generateColorList(priceTuple[0])

        # keyword count
        keywordFrequencyList = getFrequency(products) # Counts Frequency
        keywordFrequencyList = removeListOfKeywords(keywordFrequencyList) # Removes unneccessary keywords
        listOfKeywordColors = generateColorList(keywordFrequencyList) # Gets random list of colors

        return render_template('search/output.html', kw=keywords, products=keywordFrequencyList, priceResult=minMaxAvg, colors=listOfKeywordColors,
        priceColors=priceColors, priceCount=priceTuple[0],priceLabels=priceTuple[1],
        urls=productImageUrls)

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
    keywordFrequencyList = removeKeyword(keywordFrequencyList,'to')

    keywordFrequencyList = [t for t in keywordFrequencyList if len(t[0]) > 1]

    # filters kw below certain count
    countThreshold = NUMBER_OF_PRODUCTS_SEARCH / 6

    keywordFrequencyList = [t for t in keywordFrequencyList if t[1] > countThreshold]

    return keywordFrequencyList

# Prints a list item
def printList(listObject):
    for i in listObject:
        print(i)

# Gets random colors for chart
def generateColorList(keywordFrequencyList):
    colorList = []

    # Gets number of keywords in list
    keywordFrequencyCount = len(keywordFrequencyList)

    for i in range(keywordFrequencyCount):
        r = lambda: random.randint(0,255)
        colorHexCode = '#%02X%02X%02X' % (r(),r(),r())
        colorList.append(colorHexCode)

    return colorList
