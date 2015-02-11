from interfaces.bspline_vector_space import *
#from utilities import *
import numpy as np
#from numpy.linalg import lstsq
from matplotlib.pylab import *
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import scipy.integrate

# ---- 1D -----

def test_1d():
    # BSpline parameters
    n = 5 # num. of ??
    p = 3  # degree
    # Number of least square points
    n_ls = 140

    # Open knot vector
    knots = r_[p*[0], np.linspace(0,1,n), p*[1]]
    # len(knots) = m = n + 2p + 1
    print "n =", n
    print "p =", p
    print "len(knots) =", len(knots)

    vs = BsplineVectorSpace(p, knots)
    # n_dofs = n_ctrl_pts = len(knots) - p - 1

    #c = np.array([1]*(len(knots)-p-1)) # coefficients
    c = np.random.rand(len(knots)-p-1) # coefficients
    x = np.linspace(0, 1, 100)
    f = vs.element(c)
    y = f(x)

    plt.plot(x,y,'k')
    ctrl_pts_x = np.linspace(0,1,vs.n_dofs)
    print ctrl_pts_x
    #ctrl_pts_x = (ctrl_pts_x + (ctrl_pts_x[1]-ctrl_pts_x[0])*0.5)[:-1]
    #print ctrl_pts_x
    plt.plot(ctrl_pts_x,c,'ob')
    plt.show()

# ---- 2D -----

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
    plt.plot(T1,T2,'or') # knots

    plt.show()

def test_2d():
    # BSpline parameters
    n = 5 # num. of ??
    p = 3  # degree
    # Number of least square points
    n_ls = 140

    # Open knot vector
    knots = r_[p*[0], np.linspace(0,1,n), p*[1]]
    # len(knots) = m = n + 2p + 1
    print "n =", n
    print "p =", p
    print "len(knots) =", len(knots)

    vs = BsplineVectorSpace(p, knots)
    # n_dofs = n_ctrl_pts = len(knots) - p - 1

    #c = np.array([1]*(len(knots)-p-1)) # coefficients
    c = [np.random.rand(vs.n_dofs),np.random.rand(vs.n_dofs)] # coefficients

    plot_bspline_2d(vs,c)

def test_2d_constr():
    # BSpline parameters
    n = 5 # num. of ??
    p = 3  # degree
    # Number of least square points
    n_ls = 140

    # Open knot vector
    knots = r_[p*[0], np.linspace(0,1,n), p*[1]]
    # len(knots) = m = n + 2p + 1
    print "n =", n
    print "p =", p
    print "len(knots) =", len(knots)

    vs = BsplineVectorSpace(p, knots)
    # n_dofs = n_ctrl_pts = len(knots) - p - 1

    #c = np.array([1]*(len(knots)-p-1)) # coefficients
    c = [np.concatenate(([1],np.random.rand(vs.n_dofs-2),[0])),np.concatenate(([0],np.random.rand(vs.n_dofs-2),[1]))] # coefficients

    plot_bspline_2d(vs,c)

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

def test_2d_integrate():
    # BSpline parameters
    n = 5 # num. of ??
    p = 3  # degree

    # Open knot vector
    knots = r_[p*[0], np.linspace(0,1,n), p*[1]]
    # len(knots) = m = n + 2p + 1
    print "n =", n
    print "p =", p
    print "len(knots) =", len(knots)

    vs = BsplineVectorSpace(p, knots)
    # n_dofs = n_ctrl_pts = len(knots) - p - 1
    print "vs.n_dofs =", vs.n_dofs

    c = [np.concatenate(([1],np.random.rand(vs.n_dofs-2),[0])),np.concatenate(([0],np.random.rand(vs.n_dofs-2),[1]))] # coefficients

    plot_bspline_2d(vs,c)

# -------------------

if __name__=='__main__':
    test_1d()
    test_2d()
    test_2d_constr()
    test_2d_integrate()
