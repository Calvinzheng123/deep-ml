import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    abs_matrix = np.abs(arr)
    answer = 0
    # Your code here
    if norm_type == 'frobenius':
        if arr.ndim != 2:
            raise ValueError()
        answer = np.sqrt(np.sum(abs_matrix ** 2))
    elif norm_type == 'l1':
        answer += np.sum(abs_matrix)
    elif norm_type == 'l2':
        answer = np.sqrt(np.sum(abs_matrix ** 2))
    elif norm_type == 'linf':
        answer = np.max(abs_matrix)
    else:
        raise ValueError()
    

    return float(answer)
        
