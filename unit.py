import random

class unit:
    def __init__(self, genes):
        '''This class represents one individual of the population'''
        self.genes = genes
        self.fitness = None

if __name__ == '__main__':
    U1 = unit([random.randint(-10, 10) for x in range(4)])
    print(U1.genes)