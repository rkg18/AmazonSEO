from forest.info import *
import math

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
    
    minPrice = round(minPrice,2)

    return minPrice

def getMaxPrice(productList):
    maxPrice = 0

    for i in productList:
        if i > maxPrice:
            maxPrice = i

    maxPrice = round(maxPrice,2)

    return maxPrice

def getAveragePrice(productList):
    return round((sum(productList) / len(productList)),2)

def getPriceResultsList(productList):
    minMaxAvg = []

    minMaxAvg.append(getMinPrice(productList))
    minMaxAvg.append(getMaxPrice(productList))
    minMaxAvg.append(getAveragePrice(productList))

    return minMaxAvg

############# Functions to generate Chart elements ######################
def getPriceRanges(myList, maxPrice):

    rangeNumber  = maxPrice / 5
    rangeNumber  = math.ceil(rangeNumber)

    priceRangeListLabels = []
    priceRangeCount = []

    for i in range(5):
        rangeMaxNumber = (i+1) * rangeNumber
        rangeMinNumber = i * rangeNumber
        rangeLabel = str(rangeMinNumber) + " - " + str(rangeMaxNumber)

        priceRangeListLabels.append(rangeLabel) # Adds label to list

        priceCount = 0

        for y in myList:
            if(y <= rangeMaxNumber and y >= rangeMinNumber):
                priceCount += 1

        priceRangeCount.append(priceCount)

    return priceRangeCount,priceRangeListLabels