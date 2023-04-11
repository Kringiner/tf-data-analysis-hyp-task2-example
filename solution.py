import numpy as np
import pandas as pd
from scipy.stats import ks_2samp
from scipy.stats import cramervonmises_2samp
from scipy.stats import anderson_ksamp

chat_id = 843200348


def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.04
    p_val = anderson_ksamp([x, y]).pvalue
    return p_val < alpha
