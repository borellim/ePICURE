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


class Optimization(object):
    """
    An abstract optimization tool, taking an EquationOfMotion,
    computing a CostFunction associated to it, imposing a
    ConstraintEquation on it, and optimizing the Shape evolution, in
    order to obtain a Shape that satisfies the ConstraintEquation
    and minimizes the CostFunction
    """
    def __init__(self):
        pass

    def set_optimization_routine(self):
        # self.optimization_routine = ...
        # self.optimization_routine = ...
        pass

    def optimize(self):
        # Call optimization routine
        optimal_shape = Shape() #......
        return optimal_shape
