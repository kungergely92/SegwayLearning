import random

class Unit:
    def __init__(self, minValue, maxValue, randFitness=False):
        '''This class represents one individual of the population'''
        self.genes = [random.randint(minValue, maxValue) for x in range(4)]
        self.fitness = random.randint(minValue, maxValue) if randFitness else None

if __name__ == '__main__':
    U1 = Unit(-10, 10)
    print(U1.genes)