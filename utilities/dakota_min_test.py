import numpy as np

def function_to_minimize(**kwargs):
    """
    Test function for the Dakota <-> Python/numpy interface.
    Objective: find the minimum of f(x)=x^2.
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
        f = np.array([x*x])
        retval['fns'] = f

    if (ASV[0] & 2): # **** df/dx:
        g = np.array([[2*x]])
        retval['fnGrads'] = g

    if (ASV[0] & 4): # **** d^2f/dx^2:
        h = np.array([[[2]]])
        retval['fnHessians'] = h

    """
    f0 = x[1]-x[0]*x[0]
    f1 = 1-x[0]

    retval = dict([])

    if (ASV[0] & 1): # **** f:
        f = array([100*f0*f0+f1*f1])
        retval['fns'] = f

    if (ASV[0] & 2): # **** df/dx:
        g = array([[-400*f0*x[0] - 2*f1, 200*f0]])
        retval['fnGrads'] = g

    if (ASV[0] & 4): # **** d^2f/dx^2:
        fx = x[1]-3*x[0]*x[0]

        h = array([ [ [-400*fx + 2, -400*x[0]],
              [-400*x[0],    200     ] ] ]    )
        retval['fnHessians'] = h
    """

    print "Evaluation n. " + curr_eval_id

    return(retval)

