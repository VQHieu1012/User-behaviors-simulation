# utils.py

import random

def rand_chance(probability: float) -> bool:
    """
        Return True or False base on input and probability
    """
    return random.random() < probability
