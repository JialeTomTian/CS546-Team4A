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

def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """

    if x == 1: return True
    if n == 0: return x == 0
    if n == 1: return x == 1
    if n == -1: return abs(x) == 1
    p = n
    while abs(p) <= abs(x):
        if p == x: return True
        p = p * n
    return False



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


def check(candidate):
    inputs = [[16, 2], [143214, 16], [4, 2], [9, 3], [16, 4], [24, 2], [128, 4], [12, 6], [1, 1], [1, 12], [25, 5], [81, 3], [64, 4], [36, 6], [10, 2], [20, 5], [15, 3], [35, 5], [49, 7], [125, 5], [5, 5], [23, 5], [25, 23], [23, 2], [21, 2], [6, 5], [6, 7], [81, 6], [64, 6], [2, 2], [2, 5], [23, 23], [25, 6], [82, 3], [82, 7], [81, 81], [10, 3], [36, 5], [15, 23], [7, 15], [82, 2], [10, 81], [49, 8], [81, 7], [21, 35], [20, 23], [81, 25], [35, 35], [81, 5], [83, 4], [64, 21], [23, 81], [64, 64], [49, 82], [8, 6], [4, 5], [125, 2], [82, 1], [8, 64], [11, 23], [49, 4], [11, 7], [125, 6], [24, 25], [64, 5], [5, 4], [20, 19], [15, 15], [82, 5], [4, 4], [11, 11], [25, 25], [24, 10], [3, 10], [23, 15], [82, 82], [11, 10], [80, 81], [3, 2], [36, 36], [8, 5], [5, 6], [35, 49], [6, 6], [19, 5], [8, 49], [49, 49], [37, 6], [3, 4], [65, 64], [6, 81], [37, 15], [65, 5], [10, 11], [82, 65], [82, 23], [24, 23], [66, 65], [10, 10], [7, 11], [7, 25], [4, 24], [49, 3], [84, 84], [2187, 3], [8192, 4], [16777216, 4], [1099511627776, 2], [4722366482869645213696, 6], [27, 3], [243, 3], [245, 5], [65536, 2], [245, 27], [2188, 3], [4722366482869645213696, 4722366482869645213696], [245, 245], [2188, 2189], [4, 3], [2189, 2189], [4, 65536], [243, 2], [65537, 65536], [2189, 2188], [2, 6], [2187, 2189], [245, 244], [81, 2188], [16777216, 16777217], [5, 27], [243, 6], [82, 245], [3, 3], [4, 16777217], [245, 16777217], [2188, 2188], [81, 16777217], [243, 4], [245, 2188], [242, 16777216], [3, 65537], [2188, 16777216], [246, 5], [242, 1099511627776], [240, 240], [1099511627776, 2187], [2188, 2], [3, 65536], [243, 16777217], [16777217, 81], [242, 242], [6, 4722366482869645213696], [16777217, 16777216], [243, 243], [26, 27], [4722366482869645213696, 1099511627776], [4722366482869645213695, 4722366482869645213696], [245, 16777216], [2, 81], [4722366482869645213695, 4], [4, 2187], [65536, 65536], [4, 16777216], [82, 246], [16777217, 16777217], [3, 5], [65537, 5], [27, 246], [2188, 16777217], [82, 4722366482869645213696], [4722366482869645213696, 1099511627777], [4722366482869645213695, 4722366482869645213695], [2187, 244], [65537, 245], [16777216, 16777216], [4722366482869645213695, 4722366482869645213697], [65536, 65537], [4722366482869645213696, 4722366482869645213695], [243, 242], [2187, 1099511627776], [2189, 3], [1099511627775, 1099511627775], [246, 246], [65537, 3], [240, 16777216], [1099511627776, 242], [16777215, 16777216], [4722366482869645213696, 65537], [246, 245], [81, 246], [8192, 27], [16777215, 245], [16777216, 240], [246, 65536], [2187, 245], [244, 1099511627776], [5, 1], [65537, 6], [65537, 65537], [4, 1099511627775], [2, 16777217], [2188, 2187], [1099511627776, 1], [2, 4722366482869645213695], [240, 2188], [27, 16777217], [82, 4722366482869645213697], [1099511627776, 1099511627777], [4722366482869645213695, 2188], [1099511627775, 1099511627776], [2187, 2188], [1099511627775, 244], [244, 244], [246, 243], [2187, 2187], [1099511627775, 5], [4, 246], [16777215, 4], [2186, 2187], [1099511627777, 2187], [16777216, 27], [2186, 2186], [65537, 1099511627776], [2187, 16777216], [246, 16777217], [65538, 65536], [1099511627777, 3], [80, 2188], [27, 245], [83, 82], [3, 4722366482869645213695], [247, 246], [1099511627777, 4722366482869645213696], [83, 81], [4722366482869645213697, 4722366482869645213695], [5, 245], [247, 247], [246, 247], [81, 4722366482869645213696], [1, 4], [243, 65536], [244, 27], [246, 2189], [2187, 16777215], [246, 16777215], [27, 27], [4, 4722366482869645213696], [245, 2189], [5, 3], [16777216, 2188], [1099511627778, 243], [2188, 1099511627777], [27, 2188], [2188, 6], [16777216, 28], [2187, 6], [4722366482869645213696, 27], [2, 82], [245, 246], [2, 1099511627778], [16777215, 27], [4722366482869645213695, 2], [1099511627778, 241], [244, 65537], [80, 243], [1099511627777, 16777216], [241, 240], [246, 2], [8192, 1099511627778], [4722366482869645213696, 244], [246, 244], [65536, 4722366482869645213697], [2186, 3], [82, 4722366482869645213695], [246, 4722366482869645213695], [16777216, 6], [27, 28], [66, 95], [26, 246], [2187, 2186], [4722366482869645213698, 4722366482869645213695], [246, 1099511627776], [4, 2188], [66, 66], [4, 82], [81, 243], [4722366482869645213697, 4722366482869645213697], [81, 16777216], [1, 27], [95, 4], [3, 242], [241, 82], [65538, 65537], [65536, 26], [81, 65538], [1, 245], [1099511627778, 1099511627777], [2, 3], [242, 82], [240, 65537], [1099511627778, 1099511627778], [2186, 1099511627775], [244, 6], [83, 1], [8192, 8192], [2187, 242], [65537, 27], [2186, 5], [247, 4722366482869645213697], [28, 2190], [0, 1], [1099511627775, 1], [4, 80], [245, 1099511627775], [1, 2], [65538, 65538], [4722366482869645213695, 81], [4722366482869645213693, 4722366482869645213693], [241, 65538], [2187, 1099511627774], [65537, 81], [4722366482869645213696, 2187], [1099511627776, 2190], [16777215, 2188], [242, 1], [1099511627777, 1099511627777], [4722366482869645213696, 3], [96, 4], [242, 2190], [2186, 82], [242, 241], [1099511627777, 1099511627776], [16777215, 26], [65536, 5], [1099511627776, 4722366482869645213693], [2190, 241], [3, 16777217], [1099511627775, 1099511627774], [1099511627778, 4722366482869645213695], [245, 247], [16777217, 2188], [245, 4], [66, 16777214], [65537, 2185], [1, 3], [2188, 1099511627776], [65538, 244], [94, 95], [81, 82], [65537, 2188], [1099511627775, 2], [29, 243], [65537, 28], [8193, 8192], [4722366482869645213698, 2189], [244, 245], [6, 2], [1099511627778, 1099511627779], [27, 1099511627776], [2186, 4722366482869645213696], [247, 8192], [-1, 0], [1099511627776, 244], [1099511627777, 26], [6, 4], [2189, 241], [1099511627778, 2188], [1099511627774, 1], [28, 16777216], [3, 16777216], [4722366482869645213698, 246], [65537, 65538], [4722366482869645213698, 4722366482869645213698], [1099511627776, 3], [4722366482869645213696, 66], [6, 16777215], [83, 95], [8193, 2], [244, 2188], [16777218, 81], [5, 26], [81, 66], [-1, -2], [1, 244], [247, 4722366482869645213698], [2187, 65536], [1099511627774, -2], [-2, 0], [82, 27], [29, 81], [4722366482869645213693, 96], [82, 81], [2, 1099511627776], [1, 246], [81, 2187], [83, 1099511627775], [4722366482869645213695, 16777217], [80, 1099511627774], [242, 243], [82, 6], [246, 81], [243, 1099511627775], [16777217, 2185], [1099511627774, 80], [6, -2], [1, 8192], [1099511627777, 4722366482869645213695], [4722366482869645213695, 1099511627776], [4722366482869645213695, 4722366482869645213694], [27, 26], [83, 80], [4, 27], [29, 82], [1099511627778, 4722366482869645213693], [247, 28], [16777214, 16777215], [1099511627774, 242], [242, 3], [247, 1099511627776], [2188, 241], [246, 3], [80, 80], [16777215, 2], [66, 4722366482869645213696], [242, 96], [4722366482869645213694, 4722366482869645213694], [81, 16777215], [4722366482869645213694, 244], [96, 242], [1, 65537], [2189, 82], [246, 1099511627778], [-2, -2], [16777215, 16777215], [4722366482869645213696, 16777216], [2187, 1099511627775], [8193, 4], [-1, 1099511627775], [4, 65537], [16777217, 2187], [2190, 4722366482869645213695], [240, 16777217], [26, -2], [82, 4722366482869645213698], [26, 26], [4, 6], [240, 241], [1099511627778, 82], [4, 65535], [16777217, 1099511627778], [8191, 82], [16777217, 243], [96, 65537], [1099511627776, 1099511627776], [95, 96], [27, 4722366482869645213695], [244, 8191], [1099511627774, 244], [65536, 247], [243, 2189], [1099511627774, 16777215], [95, 2], [80, 3], [244, 4722366482869645213696], [4722366482869645213695, 82], [4722366482869645213695, 8193], [2190, 16777217], [247, 245], [80, 4722366482869645213694], [16777214, 27], [-2, 5], [1099511627779, 65536], [2187, 95], [241, 1099511627776], [-1, 67], [95, 95], [2190, 65536], [6, 242], [95, 4722366482869645213694], [247, 2], [241, 65536], [241, 239], [1, 1099511627778], [247, 4722366482869645213696], [244, 95], [8192, 246], [241, 66], [16777216, 65537], [244, 16777214], [97, 242], [29, 29], [3, 241], [8192, 16777216], [96, 3], [248, 2185], [241, 241], [16777215, 65536], [80, 245], [245, 95], [2187, 1099511627779], [2187, 2], [2189, 1099511627779], [67, 67], [4722366482869645213694, 4722366482869645213693], [1, 4722366482869645213695], [3, 246], [16777215, 16777214], [82, 2188], [80, 5], [80, 1099511627775], [2186, 245], [4, 2190], [4722366482869645213697, 95], [2189, 2], [67, 1099511627779], [240, 6], [4722366482869645213699, 4722366482869645213695], [4722366482869645213697, 65537], [244, 4], [81, 2], [65537, 83], [4722366482869645213696, 8192], [2190, 4722366482869645213696], [1099511627777, 1099511627778], [81, 4722366482869645213695], [8192, 8193], [246, 2188], [2189, 2190], [80, 16777216], [242, 1099511627778], [93, 93], [95, 246], [7, 7], [2190, 2190], [1099511627774, 4722366482869645213699], [241, 242], [240, 244], [248, 82], [244, 1099511627775], [65537, 82], [1099511627775, 242], [16777215, 240], [3, 244], [16777214, 16777216], [2, 27], [28, 28], [4722366482869645213696, 80], [242, 1099511627775], [247, 1099511627779], [65536, 65538], [241, 16777216], [16777216, 66], [81, 28], [2186, 16777215], [2190, 245], [1099511627776, 2191], [0, 2], [-8, 2], [16, -2], [-1, 1], [0, 0], [-1, 2], [10, -3], [3, 1000000], [101, 101], [2, 8192], [4722366482869645213695, 6], [2, 65537], [8193, 3], [3, 81], [4722366482869645213695, 16777216], [8, 8], [16777216, 4722366482869645213695], [5, 8193], [2186, 4], [8, 245], [5, 246], [65536, 4722366482869645213696], [4, 2186], [243, 65537], [28, 245], [16777216, 3], [243, 28], [8192, 245], [5, 81], [4722366482869645213695, 2186], [246, 2187], [81, 4], [6, 8193], [28, 8192], [65537, 8], [8191, 245], [244, 3], [65536, 1], [247, 2187], [65537, 2], [3, 243], [8191, 8], [2, 1], [2187, 4], [246, 4], [8190, 8191], [246, 8], [1099511627776, 4722366482869645213696], [65535, 65535], [4722366482869645213695, 2185], [245, 81], [1, 2187], [5, 2186], [1, 1099511627776], [246, 8192], [25, 26], [244, 5], [4722366482869645213694, 4722366482869645213695], [4722366482869645213695, 2187], [25, 246], [1099511627777, 2], [65536, 6], [2186, 8191], [28, 65536], [4722366482869645213696, 8], [4722366482869645213695, 5], [6, 3], [5, 65535], [3, 27], [245, 2], [243, 27], [28, 65537], [8192, 2187], [1, 8193], [2, 1099511627777], [8194, 3], [5, 8], [1099511627776, 8192], [1099511627776, 8193], [2187, 1099511627777], [4722366482869645213696, 7], [65537, 2187], [26, 3], [28, 5], [3, 4722366482869645213694], [5, 8194], [7, 6], [1099511627776, 81], [25, 3], [8192, 247], [4722366482869645213694, 3], [7, 8], [4722366482869645213695, 8194], [2, 8193], [246, 8191], [1099511627776, 2186], [243, 8192], [0, 3], [4722366482869645213694, 4722366482869645213696], [4722366482869645213694, 16777216], [7, 5], [65536, 65535], [4722366482869645213694, 2186], [7, 4], [5, 8195], [6, 8], [4722366482869645213694, 2187], [29, 5], [3, 28], [5, 8192], [2186, 1], [65537, 4722366482869645213696], [9, 8], [16777216, 1], [2187, 8195], [8190, 4722366482869645213695], [2187, 26], [1, 0], [247, 3], [5, 4722366482869645213694], [16777216, 4722366482869645213696], [247, 5], [9, 4722366482869645213694], [246, 82], [4722366482869645213695, 8195], [5, 7], [246, 2186], [25, 2186], [243, 245], [1099511627779, 2186], [8190, 27], [2187, -99], [8, 65535], [10, 9], [65536, 27], [4722366482869645213694, 9], [9, 4], [29, 3], [2185, 2185], [9, 65536], [28, 8191], [65536, 3], [4722366482869645213695, 26], [25, 1], [244, 29], [0, 82], [4722366482869645213696, 5], [4722366482869645213693, 82], [4, 4722366482869645213695], [4722366482869645213695, 65535], [2187, 7], [2, 8194], [4722366482869645213695, 9], [245, 65537], [8195, 4722366482869645213696], [29, 2185], [8, 4722366482869645213695], [247, 6], [-99, -99], [2, 7], [245, 1099511627779], [7, 2], [5, 4722366482869645213696], [8190, 7], [9, 1099511627777], [8194, 4722366482869645213696], [8195, 2187], [8, 7], [65537, 247], [6, 247], [2186, 8192], [4722366482869645213696, 65536], [4722366482869645213694, 246], [242, 245], [65538, 4722366482869645213696], [4722366482869645213695, 8], [-99, 4722366482869645213695], [28, 246], [6, 8194], [242, 1099511627779], [1099511627779, 2185], [243, 246], [2, 8191], [-75, -73], [6, 1099511627778], [-100, 4722366482869645213695], [6, 29], [8189, 8190], [242, 65537], [2, 25], [65535, 4], [8194, 8194], [3, 25], [6, 8195], [8193, 2187], [8195, 65535], [1099511627777, 8192], [1099511627779, 1], [-74, -75], [3, 247], [2186, 1099511627779], [6, 16777216], [4722366482869645213693, 4722366482869645213694], [2186, 6], [1099511627777, 65537], [8189, 8189], [7, 4722366482869645213693], [8191, 2188], [-100, -99], [246, 4722366482869645213694], [245, 8], [2187, 81], [10, -73], [8191, 247], [1099511627779, 1099511627779], [8194, 8193], [4722366482869645213695, 3], [8193, 8193], [8190, 65535], [2186, 8195], [82, 25], [26, 29], [65537, 8195], [8193, 8194], [4722366482869645213695, 8189], [2, 1099511627779], [4722366482869645213696, 9], [3, -74], [65535, 27], [8191, 65535], [8, 4722366482869645213693], [245, 65538], [8190, 8190], [245, 26], [65536, 4722366482869645213693], [50, 50], [2, -73], [6, 8192], [65536, 10], [16777216, 1099511627778], [244, 8192], [8191, 4722366482869645213693], [8192, 3], [4722366482869645213695, 65537], [8195, 8195], [4722366482869645213694, 5], [65537, 65535], [4722366482869645213696, 8195], [4722366482869645213696, 2189], [9, 8195], [2185, 4722366482869645213695], [4722366482869645213694, 2185], [7, 244], [1099511627780, -99], [8191, 8191], [65535, 65537], [-100, 4722366482869645213694], [65539, 65538], [1, 5], [16777217, 3], [27, 65536], [9, 2], [9, 9], [8193, 6], [1099511627775, 2186], [25, 1099511627778], [3, 1], [240, 65536], [1099511627780, -100], [2, 65536], [4722366482869645213696, 246], [2, 65539], [1099511627777, 65534], [29, 28], [2187, 4722366482869645213695], [-56, 81], [-74, 8192], [8, 242], [65536, 4722366482869645213694], [8, 50], [65539, 4722366482869645213695], [1099511627777, 247], [1099511627776, 16777217], [28, 3], [245, 28], [65535, 65536], [65535, 8191], [4722366482869645213696, 65535], [8192, 6], [2, 247], [246, 1], [-72, -73], [2187, 65535], [8194, 8190], [65534, 6], [2186, 8], [8193, 2188], [50, 242], [8195, 11], [245, -72], [8193, -16], [246, 1099511627779], [8190, 4], [246, 9], [4722366482869645213695, 8191], [16777216, 8191], [244, 65538], [8193, 1099511627775], [1099511627778, 1], [241, -99], [5, 2187], [6, 246], [1099511627779, 1099511627780], [65537, 8192], [2185, 2187], [4, 8191], [-101, 4722366482869645213695], [-71, -73], [29, 30], [8191, -100], [-72, 6], [1099511627777, 2186], [8190, 3], [8194, 16777217], [-99, 65535], [2, 4722366482869645213696], [7, 65536], [8190, 2187], [26, 4], [65534, 246], [1099511627780, 245], [51, 242], [65536, 29], [4, 1], [2188, -99], [-71, 2187], [8, 28], [2187, -72], [11, 2185], [4722366482869645213695, 1099511627780], [4722366482869645213697, 82], [1099511627775, 4722366482869645213695], [-56, 245], [1099511627780, -16], [243, -70], [1099511627775, 65536], [1099511627778, 5], [47, 82]]
    results = [True, False, True, True, True, False, False, False, True, True, True, True, True, True, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, True, False, True, True, False, True, True, False, True, False, False, True, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, True, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)

@measure_performance
def run():
    check(is_simple_power)
if __name__ == "__main__":
    time_used,mem_used = run()
    print(time_used,mem_used)
