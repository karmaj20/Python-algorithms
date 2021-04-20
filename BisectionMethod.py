import numpy as np
import math
# BISECTION METHOD

def f(x):
    return math.cos(x) - x

def bisectionMethod(xL, xR, eps):
    if f(xL)*f(xR) > 0.0:
        print('Root not in the given interval')

    xM = (xR + xL)/2.0
    error = np.abs((xR-xL)/xM)
    numberOfIterations = 0

    while error > eps:
        xM = (xR + xL) / 2.0
        if f(xL)*f(xM) > 0.0:
            xL = xM
        else:
            xR = xM
        error = np.abs((f(xR) - f(xL)) / xM)
        numberOfIterations += 1

    print('The score was given after {} iterations'.format(numberOfIterations))
    print('The root of function f(x) = cosx-x is in the interval <{:.8f}, {:.8f}> with accuracy {}'.format(xL,xR,eps))

def main():
    xL = float(input('Left side of the compartment: '))
    xR = float(input('Right side of the compartment: '))
    eps = float(input('Set the accuracy: '))
    bisectionMethod(xL, xR, eps)

main()