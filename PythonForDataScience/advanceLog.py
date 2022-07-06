import logging
# import mitarbeiter

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


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
    return x / y


def modulo(x, y):
    return x % y


def Main():
    num_1 = 20
    num_2 = 10

    add_result = add(num_1, num_2)
    logging.debug('ADD: {} + {} = {}'.format(num_1, num_2, add_result))

    sub_result = substract(num_1, num_2)
    logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

    mul_result = multiply(num_1, num_2)
    logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

    div_result = divide(num_1, num_2)
    logging.debug('DIV: {} / {} = {}'.format(num_1, num_2, div_result))

    mod_result = modulo(num_1, num_2)
    logging.debug('MOD: {} % {} = {}'.format(num_1, num_2, mod_result))


if __name__ == '__main__':
    Main()
