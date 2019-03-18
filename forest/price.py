from forest.info import *

def getProductPrice(productList):
    productPriceList = []

    for product in productList:
        productPriceList.append(product.price_and_currency[0])

    return productPriceList

def getMinPrice(productList):
    return min(productList)

def getMaxPrice(productList):
    return max(productList)

def getAveragePrice(productList):
    return sum(productList) / len(productList)

def getPriceResultsList(productList):
    minMaxAvg = []

    minMaxAvg.append(getMinPrice(productList))
    minMaxAvg.append(getMaxPrice(productList))
    minMaxAvg.append(getAveragePrice(productList))

    return minMaxAvg