from temperature import *
from capacity import *
from rules import *

class Controller:
    def __init__(self, temperature, capacity):
        self.rules = Rules()
        self.temp = Temperature(temperature)
        self.cap = Capacity(capacity)

    def solve(self):
        
        aggregate = self.rules.evaluate(self.temp, self.cap)

        print("power for furnance: "+sorted(list(aggregate.items()), key = lambda x: x[1])[-1][0])
        
     