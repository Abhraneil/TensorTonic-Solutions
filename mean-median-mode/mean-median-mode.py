from collections import Counter
import numpy as np
import scipy
from scipy import stats

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """

    return {"mean": float(np.mean(x)),"median": float(np.median(x)),"mode": float(stats.mode(x).mode)}
    
    pass