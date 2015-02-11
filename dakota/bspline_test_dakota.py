from interfaces.bspline_vector_space import *
#from utilities import *
import numpy as np
#from numpy.linalg import lstsq
from matplotlib.pylab import *
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import scipy.integrate


def bspline_custom_integral(vs, c):
    """ Calculates int_0^1 x^2*y, where x and y are the first
    and second coordinates of the 2D B-spline curve defined by
    the basis vs and coefficients c."""
    x = np.linspace(0, 1, 100)
    f1 = vs.element(c[0])
    f2 = vs.element(c[1])
    y1 = f1(x)
    y2 = f2(x)
    z = y1*y1 + y2

    I = scipy.integrate.simps(z, x)
    return I

def plot_bspline_2d(vs, c):
    x = np.linspace(0, 1, 100)
    f1 = vs.element(c[0])
    f2 = vs.element(c[1])
    y1 = f1(x)
    y2 = f2(x)
    T1 = f1(vs.knots)
    T2 = f2(vs.knots)

    plt.plot(y1,y2,'k')
    ctrl_pts_x = np.linspace(0,1,vs.n_dofs)
    #ctrl_pts_x = (ctrl_pts_x + (ctrl_pts_x[1]-ctrl_pts_x[0])*0.5)[:-1]
    #print ctrl_pts_x
    plt.plot(c[0],c[1],'ob') # control points
    plt.plot(T1,T2,'.r') # knots

    plt.show()

def dakota_target_function(c, plot=False):
    # BSpline parameters
    n = 5 # num. of "pseudo-internal" knots
    p = 3  # degree

    # Open knot vector
    knots = r_[p*[0], np.linspace(0,1,n), p*[1]]
    # len(knots) = m = n + 2p + 1

    vs = BsplineVectorSpace(p, knots)
    # n_dofs = n_ctrl_pts = len(knots) - p - 1

    #c = [np.concatenate(([1],np.random.rand(vs.n_dofs-2),[0])),np.concatenate(([0],np.random.rand(vs.n_dofs-2),[1]))] # coefficients

    if plot:
        plot_bspline_2d(vs, c)

    I = bspline_custom_integral(vs, c)
    print "Integral:", I
    return I

def dakota_entry_point(**kwargs):
    """
    Dakota <-> Python/numpy interface.
    Objective: ...
    """

    num_funs = kwargs['functions']
    num_vars = kwargs['variables']
    curr_eval_id = kwargs['currEvalId']
    assert num_funs==1
    assert num_vars==14 # 7 coeff, 2D
    X = kwargs['cv']
    c = np.reshape(X,(2,7))
    ASV = kwargs['asv'] # active set vector

    retval = dict([])

    if (ASV[0] & 1): # **** f:
        plot = not (curr_eval_id%200)
        f = np.array([dakota_target_function(c, plot)])
        retval['fns'] = f

    """
    if (ASV[0] & 2): # **** df/dx:
        g = np.array([[2*(x-7)]])
        retval['fnGrads'] = g

    if (ASV[0] & 4): # **** d^2f/dx^2:
        h = np.array([[[2]]])
        retval['fnHessians'] = h
    """

    print "Evaluation n. " + str(curr_eval_id)

    return(retval)


if __name__=='__main__':
    #test_1d()
    #test_2d()
    #test_2d_constr()
    test_2d_integrate()
