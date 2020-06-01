from fuz import *

class Temperature(Fuzzy):
    def __init__(self, value):
        self.value = value
        self.labels = {
            'cold': [(-np.inf, 1), (30,1), (50,0), (np.inf, 0)],
            'cool': [(-np.inf, 0), (30, 0), (50, 1), (70, 0), (np.inf, 0)],
            'moderate': [(-np.inf, 0), (60, 0), (70, 1), (80,0), (np.inf, 0)],
            'hot': [(-np.inf, 0), (70, 0), (90, 1), (110,0),(np.inf, 1)],
            'very hot':[(-np.inf, 0),(90,0),(110,1),(120,1),(np.inf, 1)]
        }