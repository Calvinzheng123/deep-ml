import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    # Your code here
    max_val = max(scores)
    exps = [np.exp(i - max_val) for i in scores]
    sum_exps = sum(exps)
    return np.log([j / sum_exps for j in exps])