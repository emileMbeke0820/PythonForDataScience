import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



# logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


class Employer:
    """Simple employee Class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employer('William', 'King')
emp2 = Employer('Nicole', 'Cochran')
emp3 = Employer('Stephanie', 'Dixon')
emp4 = Employer('Ariel', 'Robertson')
emp5 = Employer('Sergey', 'Die')
