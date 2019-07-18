import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                  format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    """Add Function"""
    return x + y

num1 = 10
num2 = 20

add_result = add(num1, num2)
logging.warning('Add: {} + {} = {}'.format(num1,num2, add_result))



