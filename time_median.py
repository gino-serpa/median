import numpy as np
import time
from tqdm import tqdm
from collections import Counter

def synthetic_series(n, bound=1000, seed=42):
    
    np.random.seed(seed)
    if bound!=1000:
        bound = int(n/2)
    series = np.random.choice(bound,n)
    
    return series


def time_some_fs():
    
    length = []
    creation = []
    py_sort = []
    np_median = []
    np_sort = [] 
    counter_creation = []

    for n in tqdm(range(9, 25)):
        series_length = 2**n
        results['length'].append(series_length)

        start = time.time()
        # Create a series
        series = synthetic_series(series_length)
        end = time.time()
        results['creation time'].append(end-start)
        
        start = time.time()
        sorted_series = sorted(series)
        end = time.time()
        results['python sort time'].append(end-start)
        
        start = time.time()
        np_median = np.median(series)
        end = time.time()
        results['np median time'].append(end-start)
        
        start = time.time()
        np_sorted_array = np.sort(series)
        end = time.time()
        results['np sort time'].append(end-start)

        start = time.time()
        counter = Counter(series)
        end = time.time()
        results['counter time'].append(end-start)


    return results