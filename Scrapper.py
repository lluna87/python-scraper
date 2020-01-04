from models.bbva_quotation import BBVAQuotation
from models.galicia_quotation import GaliciaQuotation
from models.lanacion_quotation import LaNacionQuotation
from models.patagonia_quotation import PatagoniaQuotation
from models.hipotecario_quotation import HipotecarioQuotation
import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

#BBVAQuotation().log()
#GaliciaQuotation().log()
#LaNacionQuotation().log()
#PatagoniaQuotation().log()
HipotecarioQuotation().log()
