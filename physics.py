# import numpy
from copy import deepcopy

class physicsHandler:
    def __init__(self, intitCondition, A):
        """ This class handles the physics rules and simulates the control process. """
        self.initCond = intitCondition

        self.imICool = 'Yes!'

    def simulate(self, unit):
        """ Simulates the control process with one unit. """
        # TODO implement genes
        res = deepcopy(self.initCond)
        B = unit.genes

    def calculateFitness(self, unit):
        """ Calculates the fitness of a unit. """

    def rungeKutta4(self):
        """ This method applies the rungekutta method to step. """
        pass

    def step(self, dT):
        """ Step in time """

if __name__ == '__main__':
    pass