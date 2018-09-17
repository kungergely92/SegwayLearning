import numpy as np
from copy import deepcopy
from math import pi

class physicsHandler:
    def __init__(self, initCondition, testDemands, sysParams, unit):
        """
        This class handles the physics rules and simulates the control process. "
        :param initCondition: a list, which contains the initial conditions, which are
        updated at each step. [x, xdot, phi, phidot]
        :param demand: demanded position, velocity, OR angle []
        :param sysParams: a list, containing the descriptive parameters, in this case:
        [mass length gravitational_constant]
        :param unit: A unit object
        :param dT: Time step length
        :param steps: Number of steps to be taken
        """
        self.initCond = initCondition
        self.testDemands = testDemands
        self.sysParams = sysParams
        self.ctrlParams = unit.genes
        self.dt = 0.001
        self.eqTimeLimit = 10
        self.eqCounterLimit = 2000
        self.timeHist = []

    def simulate(self, steps):
        """ Simulates the control process with one unit. """
        res = deepcopy(self.initCond)
        B = unit.genes

    def calculateFitness(self, unit):
        """ Calculates the fitness of a unit. """


        # TODO gets a unit and returns its fitness value, or just changes its fitness value (member of unit class)
        # return fitness

    def sys_equation(self, res, dem):
        """

        :param res: list of state variables: [x, xdot, phi, phidot]
        :param dem: list dema
        :return:
        """

        m = self.sysParams[0]
        l = self.sysParams[1]
        g = self.sysParams[2]

        B = self.ctrlParams
        ctrl_force = 0

        for i in range(len(B)):
            ctrl_force += B[i]*(res[i]-dem[i])

        eq_11 = -4*l*m*res[3]*res[3]*np.sin(res[2])
        eq_12 = 3*g*m*np.sin(2*res[2])
        den = -5+3*np.cos(2*res[2])

        eq_1 = ((eq_11 + eq_12 - 5*ctrl_force + 3*np.cos(2*res[2])*ctrl_force) /
                (m*den))
        eq_2 = (6 * (-2 * g + l * res[3] * res[3] * np.cos(res[2])) * np.sin(res[2]) /
                (l * den))

        return np.array([res[1],
                        eq_1,
                        res[3],
                        eq_2])

    def rungeKutta4(self, dt, demand):
        """ This method applies the rungekutta method to the system equation with  . """
        ic = deepcopy(self.initCond)

        k_1 = dt * self.sys_equation(ic, demand)
        ic_1 = ic + 0.5*k_1

        k_2 = dt * self.sys_equation(ic_1, demand)
        ic_2 = ic + 0.5*k_2

        k_3 = dt * self.sys_equation(ic_2, demand)
        ic_3 = ic + k_3

        k_4 = dt * self.sys_equation(ic_3, demand)

        return ic + (1/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)

    def runTests(self):
        """ This method calls the 'rungeKutta4' method 'steps' times"""


        n = 0
        while n <= self.eqCounter:

            self.timeHist.append(self.rungeKutta4())
            self.initCond = self.rungeKutta4()
            n += 1

    def test(self, dt, demand, tolerance):

        n = 0
        eqcounter = 0

        testcase = demand[np.nonzero(demand)][0]

        if testcase is 0:
            if n*dt is self.eqTimeLimit:
                return float('nan')
            else:
                while n*dt < self.eqTimeLimit:

                    if eqcounter is self.eqCounterLimit:
                        return n*dt
                        break

                    else:
                        self.initCond = self.rungeKutta4(dt, demand)
                        self.timeHist.append([self.initCond, n*dt])

                        if (abs(self.initCond[0] - demand[0]) <= abs(tolerance[0]) and
                                abs(self.initCond[2] - demand[2]) <= abs(tolerance[2])):
                            n += 1
                            eqcounter += 1
                        elif abs(self.initCond[2]) >= pi:
                            return float('nan')
                            break
                        else:
                            n += 1




if __name__ == '__main__':

    from unit import unit

    u = unit([0.7, 0.5, 0.3, 0.3])
    ic = np.array([0, 0, 0.5, 0])
    params = [1, 1, 9.81]
    dt = 0.01
    steps = 5

    p = physicsHandler(ic, params, u, dt, steps)

    p.run()
