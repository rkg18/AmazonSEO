# Amazon Product Researcher
# Input: Product Keyword
# Output: PDF file with first page product info and what could be improved to rank

from functions import *
from amazon.api import AmazonAPI

keywords='earphones'

amazon = AmazonAPI('AKIAIDMLCQFWH64BE5KA','vNpc7x047m9ez18Zfw/90/s6jVj6okixTAr/3QNt','beyourshelves-20')

# Gets first page results for top amazon products
products = amazon.search_n(10,Keywords=keywords, SearchIndex='All')

commonStrings(products)