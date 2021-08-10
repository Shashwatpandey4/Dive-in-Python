import logging

logging.basicConfig(filename='Logging/log1.log',level=logging.DEBUG,
format='%(asctime)s : %(levelname)s : %(message)s')

def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

a=5
b=7

add_result = add(a,b)
logging.debug('Add result : {} + {} = {} '.format(a,b,add_result))

multi_result = multiply(a,b)
logging.debug('Multiply result : {} + {} = {} '.format(a,b,multi_result))
