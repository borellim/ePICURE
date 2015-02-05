import numpy as np

from interfaces.shape import Shape
from interfaces.position import Position
from interfaces.equation_of_motion import EquationOfMotion
from interfaces.optimization_routines import *


class Optimization(object):
    """
    An abstract optimization tool, taking an EquationOfMotion,
    computing a CostFunction associated to it, imposing a
    ConstraintEquation on it, and optimizing the Shape evolution, in
    order to obtain a Shape that satisfies the ConstraintEquation
    and minimizes the CostFunction
    """
    # Static dictionary of optimization routines
    all_routines = { "dakota" : OptimizationRoutineDakota,
                     "scipy"  : OptimizationRoutineScipy,
                   }

    def __init__(self):
        pass

    def set_optimization_routine(self,routine_name,routine_parameters):
        self.optimization_routine = all_routines[routine_name](routine_parameters)
        pass

    def optimize(self):
        # Call optimization routine
        optimal_shape = self.optimization_routine.optimize()
        return optimal_shape
