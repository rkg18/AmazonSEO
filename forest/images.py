from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)

from forest.info import *
import os
import urllib.request
import requests

def downloadProductImages(productList):
    for x in range(9):
        productName = spliceProductName(productList[x].large_image_url)

        fullfilename = os.path.join('images', productName)

        with open(fullfilename, 'wb') as f:
            f.write(requests.get(productList[x].large_image_url).content)

def spliceProductName(productURL):
    tempStr = str(productURL)

    startIndex = tempStr.find("/I/") + 3
    endIndex = len(tempStr)

    productName = tempStr[startIndex:endIndex]

    return productName

def getProductUrl(productList):
    urls = []

    for x in range(9):
        urls.append(productList[x].large_image_url)

    return urls