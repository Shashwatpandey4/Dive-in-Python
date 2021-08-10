# this module contains activation function implementations 
from math import exp
import logging

formatter = logging.Formatter('%(name)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('Logging/log2.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#Rectified Linear Unit (ReLU)
def relu(x):
    return max(0.0,x)

#Sigmoid
def sigmoid(x):
    return 1.0/(1.0 + exp(-x))

#Tanh
def tanh(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))


a = 50

rel = relu(a)
sig = sigmoid(a)
tan = tanh(a)

logger.info('ReLU of {} : {}'.format(a,rel))
logger.info('Sigmoid of {} : {}'.format(a,sig))
logger.info('Tanh of {} : {}'.format(a,tan))