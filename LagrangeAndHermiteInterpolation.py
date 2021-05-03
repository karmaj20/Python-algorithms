import math

def f(x):
    return math.exp(x)

def lagrangeInterpolation(xT, x, n, NbStep):
    print('Lagrange p(x):')
    for step in range(NbStep):  # loop over x
        p = 0.0
        for j in range(n - 1):  # index in xT[] from 0 to n - 1
            l_jn = 1.0
            for i in range(n - 1):
                if i != j:
                    l_jn = l_jn *((x-xT[i])/(xT[j] - xT[i]))    # calculate l_jn
            p = p + l_jn * f(xT[j])
        print('x={} p(x)={}'.format(x, p))
        x = x + 0.1

def hermiteInterpolation(xT, x, n, NbStep):
    print('Hermite p(x):')
    for step in range(NbStep):
        p = 0.0
        for j in range(n - 1):  # index in xT[] from 0 to n - 1
            l_jn = 1.0
            l_jnP = 0.0
            for i in range(n - 1):
                if i != j:
                    l_jn = l_jn * ((x - xT[i]) / (xT[j] - xT[i]))  # calculate l_jn
                    l_jnP = l_jnP + (1.0 / (xT[j] - xT[i]))  # calculate l_jn'(x_j)
            h_jn = (1.0 - 2.0 * (x - xT[j]) * l_jnP) * l_jn * l_jn
            hBar_jn = (x - xT[j]) * l_jn * l_jn
            p = p + h_jn * f(xT[j]) + hBar_jn * f(xT[j])
        print('x={} p(x)={}'.format(x, p))
        x = x + 0.1

def main():
    xT = [-1.0, 0.5, 1.5, 2.0]
    x = -5.0                    # initial value of x
    n = 4                       # number of points
    NbStep = int(10.000001/0.1) # number of steps
    lagrangeInterpolation(xT, x, n, NbStep)
    hermiteInterpolation(xT, x, n, NbStep)

if __name__ == '__main__':
    main()