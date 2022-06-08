import logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika.log')
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def dalyba(a, b):
    try:
        rezultatas = a / b

    except ZeroDivisionError:
        logger.exception("Dalyba is nulio")
    else:
        return rezultatas

a = 20
b = 0

padalinom = dalyba(a, b)
logger.info(f"Dalyba: {a} / {b} = {padalinom}")