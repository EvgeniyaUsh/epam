"""
Here's a not very efficient calculation function that calculates something important:

import time
import struct
import random
import hashlib

def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))
    
Calculate total sum of slow_calculate() of all numbers starting from 0 to 500. Calculation time should not take more than a minute. 
Use functional capabilities of multiprocessing module. You are not allowed to modify slow_calculate function.
"""


import concurrent.futures
import hashlib
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def sum_of_slow_calculations():
    """
    the function calculates the total slow_calculate()
    sum of all numbers from 0 to 500 using the functionality
    of the multiprocessor module.
    The computation time does not take more than a minute.
    :return: sum of all numbers from 0 to 500
    """
    time_before = time.time()
    argument = range(500)
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        summa = sum(executor.map(slow_calculate, argument))
    time_after = time.time()
    assert time_after - time_before <= 60
    return summa
