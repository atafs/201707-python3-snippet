import logging

logging.basicConfig(filename='logger.log',level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

arg = 'i am here'
logging.debug('This message should go to the log file [%s]', arg)
