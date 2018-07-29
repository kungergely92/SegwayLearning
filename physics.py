import numpy as np
from copy import deepcopy

class physicsHandler:
    def __init__(self, initCondition, sysParams, unit, dT, steps):
        """
        This class handles the physics rules and simulates the control process. "
        :param initCondition: Contains the initial conditions, which are
        updated at each step
        :param sysParams: a list, containing the descriptive parameters, in this case:
        [mass length gravitational_constant]
        :param unit: A unit object
        :param dT: Time step length
        :param steps: Number of steps to be taken
        """
        self.initCond = initCondition
        self.sysParams = sysParams
        self.ctrlParams = unit.genes
        self.dt = dT
        self.steps = steps

    def simulate(self, steps):
        """ Simulates the control process with one unit. """
        res = deepcopy(self.initCond)
        B = unit.genes

    def calculateFitness(self, unit):
        """ Calculates the fitness of a unit. """
        # TODO gets a unit and returns its fitness value, or just changes its fitness value (member of unit class)
        # return fitness

    def sys_equation(self, res):

        m = self.sysParams[0]
        l = self.sysParams[1]
        g = self.sysParams[2]

        B = self.ctrlParams

        ctrl_f = (B[0] * res[0] + B[1] * res[1]) / m
        eq_1 = ((-2 * l * res[3] * res[3] + 3 * g * np.cos(res[2]) * np.sin(res[2])) /
                (-4 + 3 * np.cos(res[2] * np.cos(res[2]))))
        eq_2 = (6 * (-2 * g + l * res[3] * res[3] * np.cos(res[2])) * np.sin(res[2]) /
                (l * (-5 * np.cos(2 * res[2]))))

        return np.array([res[1],
                        ctrl_f + eq_1,
                        res[3],
                        eq_2])

    def rungeKutta4(self):
        """ This method applies the rungekutta method to the system equation with  . """
        ic = deepcopy(self.initCond)

        k_1 = self.dt * self.sys_equation(ic)
        ic_1 = ic + 0.5*k_1

        k_2 = self.dt * self.sys_equation(ic_1)
        ic_2 = ic + 0.5*k_2

        k_3 = self.dt * self.sys_equation(ic_2)
        ic_3 = ic + k_3

        k_4 = self.dt * self.sys_equation(ic_3)

        return ic + (1/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)

    def run(self):
        """ This method calls the 'rungeKutta4' method 'steps' times"""

        n = 0
        while n <= self.steps:

            self.initCond = self.rungeKutta4()
            n += 1


if __name__ == '__main__':

    from unit import unit

    u = unit([0.7, 0.5])
    ic = [0, 0, 0.5, 0]
    params = [1, 1, 9.81]
    dt = 0.01
    steps = 5

    p = physicsHandler(ic, params, u, dt, steps)
