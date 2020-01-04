from bs4 import BeautifulSoup
import commons.source_urls
import logging
import datetime
import requests

class BBVAQuotation():

    def __set_url(self):
        self.url = commons.source_urls.BBVA

    def __parsing(self, soup):
        cells = soup.findAll('tr')[1].findAll('td')
        self.buying = float(cells[1].findAll('span')[0].string.replace(',', '.'))
        self.selling = float(cells[2].findAll('span')[0].string.replace(',', '.'))

    def log(self):
        logging.info('Cotizacion BBVA')
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
