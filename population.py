import unit
import physics


class PopulationHandler:
    def __init__(self, size):
        self.generations = []
        self.generations.append([unit.Unit(-10, 10, randFitness=True) for x in range(size)])
        self.pHandler = physics.physicsHandler(1,1)


    def newGeneration(self, generation=None):
        """ Creating a new generation from the last one. """
        if not generation:
            generation = self.generations[-1]

        for unit in generation:
            if not unit.fitness:
                self.pHandler.calculateFitness(unit)

        self.bubbleSort(generation)


    def bubbleSort(self, gen):
        """ This method goes through a generation and swaps two units in the list if they are in the wrong order. """
        areWeCool = True
        n = len(gen)
        for j in range(n):
            for i in range(0, n-j-1):
                if gen[i].fitness > gen[i+1].fitness:
                    gen[i], gen[i+1] = gen[i+1], gen[i]
                    areWeCool = False
            if areWeCool:
                break

    def mutate(self):
        pass


if __name__ == '__main__':
    p = PopulationHandler(10)
    p.newGeneration()
    for unit in p.generations[0]:
        print(unit.fitness)
    pass
