import numpy as np

def parabola(**kwargs):
    """
    Test for the Dakota <-> Python/numpy interface.
    Objective: find the minimum of f(x)=(x-7)^2.
    """

    num_funs = kwargs['functions']
    num_vars = kwargs['variables']
    curr_eval_id = kwargs['currEvalId']
    assert num_funs==1
    assert num_vars==1
    X = kwargs['cv']
    x = X[0]
    ASV = kwargs['asv'] # ????

    retval = dict([])

    if (ASV[0] & 1): # **** f:
        f = np.array([(x-7)*(x-7)])
        retval['fns'] = f

    if (ASV[0] & 2): # **** df/dx:
        g = np.array([[2*(x-7)]])
        retval['fnGrads'] = g

    if (ASV[0] & 4): # **** d^2f/dx^2:
        h = np.array([[[2]]])
        retval['fnHessians'] = h


    print "Evaluation n. " + str(curr_eval_id)

    return(retval)

