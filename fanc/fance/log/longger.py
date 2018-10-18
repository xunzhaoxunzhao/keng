import logging
import time,datetime

def Log(msg):
    shijian =datetime.datetime.now().strftime("%Y_%m_%d_%H")
    logger=logging.getLogger(__name__)
    # logger.handlers.clear()
    logger.setLevel(level=logging.INFO)
    handler=logging.FileHandler(r'E:\Users\yz\PycharmProjects\untitled3\fance\log\%s.txt'%shijian)
 #   handler.setLevel(level=logging.INFO)
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    console=logging.StreamHandler()
    # console.setLevel(level=logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.setLevel(level=logging.INFO)
    logger.info(msg)
    logger.removeHandler(console)
    logger.removeHandler(handler)

    return logger
