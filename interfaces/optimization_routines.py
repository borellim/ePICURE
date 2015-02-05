import numpy as np

from interfaces.shape import Shape
from interfaces.position import Position
from interfaces.equation_of_motion import EquationOfMotion


class OptimizationRoutine(object):
    """
    An abstract interface to an optimization routine:
    specializations of this class will implement the method
    "optimize" to perform the actual optimization, and will
    store all necessary parameters for its correct execution.
    """
    def __init__(object):
        pass


class OptimizationRoutineDakota(OptimizationRoutine):
    """
    An actual optimization interface for Dakota.
    """
    def __init__(self,parameters):
        # self.parameter0 = parameters[0]
        # ecc.
        pass

    def optimize(self):
        # solution = ....
        # return solution
        pass


class OptimizationRoutineScipy(OptimizationRoutine):
    """
    An example optimization interface for Scipy.
    """
    def __init__(self,parameters):
        pass

    def optimize(self):
        pass
