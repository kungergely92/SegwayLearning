from unit import unit
from physics import physicsHandler
import random

class populationHandler:
    def __init__(self):
        """ This class handles the populations, generates the generations."""
        self.generations = []
        self.pHandler = physicsHandler(1,1)

    def initFirstGen(self, size):
        """ Initialize first generation. """
        self.generations.append([unit([random.randint(-10, 10) for x in range(4)]) for x in range(size)])


    def newGeneration(self, generation=None):
        """ Creating a new generation from the last one. """
        if not generation:
            generation = self.generations[-1]

        for unit in generation:
            if not unit.fitness:
                self.pHandler.calculateFitness(unit)

        self.bubbleSort(generation)
        # TODO we now have a organized generation and need to generate a new one

    def fuckFest(self, oldGen):
        """ This method gives birth to the new generation."""
        newGen = []
        # TODO implement
        return newGen

    def fuck(self, parent_1, parent_2):
        """ This method mixes the genes of the parents by a certain rule. """
        newGenes = None # yet
        # TODO implement
        child = unit(newGenes)
        return child

    def bubbleSort(self, gen):
        """ This method goes through a generation and swaps two units in the list if they
            are in the wrong order. The result is the sorted array with the most fitted unit last.
        """
        areWeCool = True
        n = len(gen)
        for j in range(n):
            for i in range(0, n-j-1):
                if gen[i].fitness > gen[i+1].fitness:
                    gen[i], gen[i+1] = gen[i+1], gen[i]
                    areWeCool = False
            if areWeCool:
                break



if __name__ == '__main__':
    p = populationHandler()
    p.initFirstGen(10)
    for unit in p.generations[0]:
        unit.fitness = random.randint(-10, 10)
    p.newGeneration()
    for unit in p.generations[0]:
        print(unit.fitness)
    pass
