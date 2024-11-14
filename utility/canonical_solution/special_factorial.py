# -*- coding: utf-8 -*-
import psutil
import os
import time
from functools import wraps
def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())

        start_time = time.perf_counter()
        start_mem = process.memory_info().rss / 1024  # KB

        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        end_mem = process.memory_info().rss / 1024

        time_used = end_time - start_time
        mem_used = end_mem - start_mem

        return time_used*1_000_000,mem_used

    return wrapper

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

    fac, ans = 1, 1
    for i in range(2, n + 1):
        fac *= i
        ans *= fac
    return ans

import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        assert np.allclose(out, exp, rtol=1e-07, atol=atol)
    else:
        assert exact_match


def ref_func(n):


    fac, ans = 1, 1
    for i in range(2, n + 1):
        fac *= i
        ans *= fac
    return ans



def check(candidate):
    inputs = [[4], [5], [7], [1], [2], [3], [6], [8], [10], [13], [20], [50], [15], [12], [11], [22], [14], [9], [21], [51], [30], [29], [32], [49], [77], [52], [23], [48], [19], [33], [16], [53], [27], [34], [35], [17], [28], [26], [47], [74], [24], [36], [95], [18], [31], [45], [37], [38], [46], [78], [39], [73], [75], [79], [80], [72], [81], [25], [76], [96], [44], [94], [40], [43], [93], [71], [42], [83], [41], [70], [97], [84], [54], [85], [92], [91], [55], [82], [69], [98], [86], [56], [99], [57], [100], [101], [58], [87], [68], [62], [59], [102], [103], [60], [88], [67], [66], [104], [63], [200], [500], [199], [198], [499], [197], [497], [501], [498], [502], [496], [201], [503], [495], [493], [196], [492], [195], [202], [504], [505], [203], [491], [204], [105], [90], [494], [89]]
    for i, inp in enumerate(inputs):
        assertion(candidate(*inp), ref_func(*inp), 0)

@measure_performance
def run():
    check(special_factorial)
if __name__ == "__main__":
    time_used,mem_used = run()
    print(time_used,mem_used)
