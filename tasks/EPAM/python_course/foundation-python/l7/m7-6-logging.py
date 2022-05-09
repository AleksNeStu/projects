#1
# a) random print output
# b) sensitive data in prod to logging
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('Debug message.')
logging.info('Info message.')
print('Print message.')

# python3 /Projects/sessions/s7/m7-6-logging.py

# python3 /Projects/sessions/s7/m7-6-logging.py 2>/dev/null
# 2>/dev/null - TALK



#2-1 TALK DEBUG
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL




#2-2 examples of output
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')




#2-3 Basic Configurations
#2-3-1 pep8 naming err
#2-3-2 log level
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')



#2-3-3 to file
import logging

logging.basicConfig(
    filename='app.log', filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


#2-3-4 formating 1
import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')

#https://docs.python.org/3/library/logging.html#logrecord-attributes

#2-3-4 formating date time
import logging

logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')

#2-3-5 additionly

