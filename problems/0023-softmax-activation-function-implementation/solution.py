import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_val = max(scores)
    exps = [math.exp(i - max_val) for i in scores]
    sum_exps = sum(exps)
    return [j / sum_exps for j in exps]
    pass