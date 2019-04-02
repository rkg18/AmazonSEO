from forest.info import *

def getProductPrice(productList):
    productPriceList = []

    for product in productList:
        productPriceList.append(product.price_and_currency[0])

    return productPriceList

def getMinPrice(productList):
    minPrice = 999999

    for i in productList:
        if i < minPrice:
            minPrice = i
    
    return minPrice

def getMaxPrice(productList):
    maxPrice = 0

    for i in productList:
        if i > maxPrice:
            maxPrice = i

    return maxPrice

def getAveragePrice(productList):
    return sum(productList) / len(productList)

def getPriceResultsList(productList):
    minMaxAvg = []

    minMaxAvg.append(getMinPrice(productList))
    minMaxAvg.append(getMaxPrice(productList))
    minMaxAvg.append(getAveragePrice(productList))

    return minMaxAvg
