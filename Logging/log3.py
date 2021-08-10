from math import exp
import log2
import logging

formatter = logging.Formatter('%(name)s : %(levelname)s : %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('Logging/log2.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


#Rectified Linear Unit (ReLU)
def relu(x):
    return max(0.0,x)

#Sigmoid
def sigmoid(x):
    return 1.0/(1.0 + exp(-x))

#Tanh
def tanh(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

#division
def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result

a = 50
b = 0

rel = relu(a)
sig = sigmoid(a)
tan = tanh(a)
div = divide(a,b)

logger.debug('ReLU of {} : {}'.format(a,rel))
logger.debug('Sigmoid of {} : {}'.format(a,sig))
logger.debug('Tanh of {} : {}'.format(a,tan))

