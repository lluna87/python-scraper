from bs4 import BeautifulSoup
import commons.source_urls
import logging
import datetime
import requests

class GaliciaQuotation():

    def __set_url(self):
        self.url = commons.source_urls.BBVA

    def __parsing(self, soup):
        row = soup.find("li", {"id": "Badge_0"})
        buyingDiv = row.findAll('div', { "data-dojo-attach-point": "buyNode" })
        sellingDiv = row.findAll('div', { "data-dojo-attach-point": "sellNode" })
        self.buying = float(buyingDiv[0].string.replace(',', '.'))
        self.selling = float(sellingDiv[0].string.replace(',', '.'))

    def log(self):
        logging.info('Cotizacion Galicia')
        logging.info('Compra: ' + str(self.buying))
        logging.info('Venta: ' + str(self.selling))

    def __init__(self):
        self.timestamp = datetime.datetime.now()
        try:
            self.__set_url()
            self.__parsing(BeautifulSoup(requests.get(self.url).text, "html.parser"))
        except:
            self.buying = None
            self.selling = None
