import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    norms = np.linalg.norm(X, axis = 1, keepdims = True)
    norms[norms == 0] = 1.0
    X_norm = X / norms

    return X_norm @ X_norm.T
    pass