import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
    """
    Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
    
    Args:
        x: Input value
        
    Returns:
        Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
    """
    # Your code here
    sigmoid = 1 / (1 + np.exp(-x))
    tanh = np.tanh(x)
    relu = np.maximum(0, x)
    if relu > 0:
        relu = 1
    result = {}
    result['sigmoid'] = float(sigmoid * (1 - sigmoid))
    result['tanh'] = float(1 - tanh ** 2)
    result['relu'] = float(relu)
    
    return result

