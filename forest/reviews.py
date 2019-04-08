from bs4 import BeautifulSoup
import requests

def getReviewCount(amazonAsin):
    url = "https://www.amazon.com/dp/" + str(amazonAsin) + "/"

    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    test = page_content.find(id = "acrCustomerReviewText")
    
    output = test.text

    print(output)
    return output