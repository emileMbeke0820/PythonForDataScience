import logging
import mitarbeiter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

stream_handler = logging.StreamHandler()

file_handler = logging.FileHandler('calculate.log')
file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    """"Addition"""
    return x + y


def substract(x, y):
    """Subtraction"""
    return x - y


def multiply(x, y):
    """"Multiplication"""
    return x * y


def divide(x, y):
    """Division"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


def modulo(x, y):
    return x % y


# logging.basicConfig(filename='calculate.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logger.debug('ADD: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = substract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('DIV: {} / {} = {}'.format(num_1, num_2, div_result))

mod_result = modulo(num_1, num_2)
logger.debug('MOD: {} % {} = {}'.format(num_1, num_2, mod_result))




