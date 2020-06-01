from fuz import *

class Capacity(Fuzzy):
    def __init__(self, value):
        self.value = value
        self.labels = {
            'small': [(-np.inf, 1), (0, 1), (5, 0), (np.inf, 0)],
            'medium': [(-np.inf, 0), (3, 0), (5, 1), (7, 0), (np.inf, 0)],
            'high': [(-np.inf, 0), (5, 0), (10, 1),  (np.inf, 1)]
        }