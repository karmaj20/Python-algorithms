import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * math.exp(x)


def initialize(X=[], Y=[]):
    for i in range(10):
        X.append(0)
        Y.append(0)
    return X, Y


def fpForward():
    X, Y = [], []
    X, Y = initialize(X, Y)
    S1, S2, S3, S4 = 0.0, 0.0, 0.0, 0.0
    h, fp, E, Exact = 0.0, 0.0, 0.0, 0.0
    Et, ht = [], []
    print('Calculation of f\'(2) with forward formula: ')
    Exact = math.exp(2.0) + 2.0 * math.exp(2.0)
    h = 0.05
    for i in range(10):
        fp = (f(2.0 + h) - f(2.0)) / h
        print('h={} fp={}'.format(h, fp))
        E = math.fabs(fp-Exact)
        X[i] = math.log(h)
        Y[i] = math.log(E)
        Et.append(E)
        ht.append(h)
        h += 0.05
    print('Exact= {:.12f}'.format(Exact))
    for i in range(10):
        S1 = S1+X[i]*Y[i]
        S3 = S3+X[i]*X[i]
        S4 = S4+X[i]
        for j in range(10):
            S2 = S2 + X[i]*Y[j]
    print('Order of the error: {}'.format((10.0*S1-S2)/(10.0*S3-S4*S4)))
    return ht, Et

def fpCentral():
    X, Y = [], []
    X, Y = initialize(X, Y)
    S1, S2, S3, S4 = 0.0, 0.0, 0.0, 0.0
    h, fp, E, Exact = 0.0, 0.0, 0.0, 0.0
    Et, ht = [], []
    print('Calculation of f\'(2) with central formula: ')
    Exact = math.exp(2.0) + 2.0 * math.exp(2.0)
    h = 0.05
    for i in range(10):
        fp = (f(2.0+h) - f(2.0-h))/(2.0*h)
        print('h={} fp={}'.format(h, fp))
        E = math.fabs(fp-Exact)
        X[i] = math.log(h)
        Y[i] = math.log(E)
        Et.append(E)
        ht.append(h)
        h += 0.05

    print('Exact={:.12f}'.format(Exact))
    for i in range(10):
        S1 = S1 + X[i]*Y[i]
        S3 = S3 + X[i]*X[i]
        S4 = S4 + X[i]
        for j in range(10):
            S2 = S2+X[i]*Y[j]
    print('Order of the error: {}'.format((10.0*S1-S2)/(10.0*S3-S4*S4)))
    return ht, Et

def fppForward():
    X, Y = [], []
    X, Y = initialize(X, Y)
    S1, S2, S3, S4 = 0.0, 0.0, 0.0, 0.0
    h, fpp, E, Exact = 0.0, 0.0, 0.0, 0.0
    Et, ht = [], []
    print('Calculation of f\'\'(2) with forward formula: ')
    Exact = 4.0*math.exp(2.0)
    h = 0.05
    for i in range(10):
        fpp = (f(2.0)-2.0*f(2.0+h) + f(2.0+2.0*h))/(h**2)
        print('h={} fpp={}'.format(h, fpp))
        E = math.fabs(fpp-Exact)
        X[i] = math.log(h)
        Y[i] = math.log(E)
        Et.append(E)
        ht.append(h)
        h += 0.05
    print('Exact={:.12f}'.format(Exact))
    for i in range(10):
        S1 = S1 + X[i]*Y[i]
        S3 = S3 + X[i]*X[i]
        S4 = S4 + X[i]
        for j in range(10):
            S2 = S2 + X[i]*Y[j]
    print('Order of the error: {}'.format((10.0*S1-S2)/(10.0*S3-S4*S4)))
    return ht, Et

def fppCentral():
    X, Y = [], []
    X, Y = initialize(X, Y)
    S1, S2, S3, S4 = 0.0, 0.0, 0.0, 0.0
    h, fpp, E, Exact = 0.0, 0.0, 0.0, 0.0
    Et, ht = [], []
    print('Calculation of f\'\' with central formula:')
    Exact = 4.0*math.exp(2.0)
    h = 0.05
    for i in range(10):
        fpp = (f(2.0+h)-2.0*f(2.0)+f(2.0-h))/(h*h)
        print('h={} fpp={}'.format(h, fpp))
        E = math.fabs(fpp-Exact)
        X[i] = math.log(h)
        Y[i] = math.log(E)
        Et.append(E)
        ht.append(h)
        h += 0.05

    print('Exact={:.12f}'.format(Exact))
    for i in range(10):
        S1 = S1 + X[i]*Y[i]
        S3 = S3 + X[i]*X[i]
        S4 = S4 + X[i]
        for j in range(10):
            S2 = S2 + X[i] * Y[j]
    print('Order of the error: {}'.format((10.0*S1-S2)/(10.0*S3-S4*S4)))
    return ht, Et

def plot():
    x1, y1 = fpForward()
    x2, y2 = fpCentral()
    x3, y3 = fppForward()
    x4, y4 = fppCentral()
    ax1 = plt.subplot(221)
    ax2 = plt.subplot(222)
    ax3 = plt.subplot(223)
    ax4 = plt.subplot(224)

    ax1.plot(np.log(x1),np.log(y1))
    ax2.plot(np.log(x2),np.log(y2))
    ax3.plot(np.log(x3),np.log(y3))
    ax4.plot(np.log(x4),np.log(y4))
    plt.tight_layout()
    plt.show()


def main():
    print('Menu: (1) f\'(x) with Forward ; (2)f\'(x) with Central')
    print('Menu: (3) f\'\'(x) with Forward ; (4)f\'\'(x) with Central')
    choice = int(input('Your choice'))
    if choice == 1:
        fpForward()
    elif choice == 2:
        fpCentral()
    elif choice == 3:
        fppForward()
    elif choice == 4:
        fppCentral()
    else:
        print('Wrong choice')
    plot()

if __name__ == '__main__':
    main()
