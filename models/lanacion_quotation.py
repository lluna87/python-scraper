from bs4 import BeautifulSoup
import commons.source_urls
import logging
import datetime
import requests

class LaNacionQuotation():

    def __set_url(self):
        self.url = commons.source_urls.LaNacion

    def __parsing(self, soup):
        currencyBox = soup.find("div", {"id": "billetes"})
        cells = soup.findAll('tbody')[0].findAll('tr')[0].findAll('td')
        self.buying = float(cells[1].string.replace(',', '.'))
        self.selling = float(cells[2].string.replace(',', '.'))

    def log(self):
        logging.info('Cotizacion La Nacion')
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
