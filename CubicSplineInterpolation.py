import math
import matplotlib.pyplot as plt
n = 11

def initializeLists(xj, a, b, c, r, pjPP, pj, Beta, Rho):
    for i in range(n):
        xj.append(0)
        a.append(0)
        b.append(0)
        c.append(0)
        r.append(0)
        pjPP.append(0)
        pj.append(0)
        Beta.append(0)
        Rho.append(0)

def f(x):
    return 1.0 / (1.0 + x * x)

def main():
    # initial lists
    xj, a, b, c, r, pjPP, pj, Beta, Rho = [], [], [], [], [], [], [], [], []
    initializeLists(xj, a, b, c, r, pjPP, pj, Beta, Rho)

    # initial values
    h = 1.0

    # initial values for pj and xj
    xj[0] = -5.0

    for i in range(n):
        if i > 0:
            xj[i] = xj[i - 1] + h
            pj[i] = f(xj[i])

    # initial values for r
    r[0] = 0.0
    r[n-1] = 0.0
    for i in range(1,n-1):
        r[i] = (6.0/h)*(pj[i+1]-2.0*pj[i]+pj[i-1])

    # initial values for a, b, c
    a[0] = 0.0
    a[1] = 0.0
    a[n-1] = 0.0
    j = 2
    while j < n - 1:
        a[j] = h
        j += 1

    b[0] = 1.0
    b[n-1] = 0.0
    for i in range(1,n-1):
        b[i] = 4.0 * h

    c[0] = 0.0
    c[n-2] = 0.0
    c[n-1] = 0.0 # not used
    for i in range(1,n-2):
        c[i] = h

    # Gaussian Elimination
    Beta[0] = b[0]
    Rho[0] = r[0]
    for i in range(1,n):
        Beta[i] = b[i] - (a[i]/Beta[i-1])*c[i-1]
        Rho[i] = r[i] - (a[i]/Beta[i-1])*Rho[i-1]

    # pjPP[n-1] = Rho[n-1]/Beta[n-1]
    j = 2
    while j <= n:
        pjPP[n-j] = (Rho[n-j] - c[n-j]*pjPP[n-j + 1]) / Beta[n-j]
        j += 1

    # print pjPP
    for i in range(n):
        print('p{}PP= {}'.format(i+1,pjPP[i]))

    # calculation of the polynomial
    x = -5.0
    xR = xj[1] # initial interval xj[0] xj[1]
    j = 0
    holdValuesp = []
    holdValuesx = []
    holdValuesfx = []
    while x < 5.0001:
        if x > xR: # jump to next interval
            j += 1
            xR = xj[j+1]
        p = pj[j] + ((pj[j+1] - pj[j])/h-(h*pjPP[j+1])/6.0-(h*pjPP[j])/3.0)*(x-xj[j])
        p = p + (pjPP[j]/2.0)*(x-xj[j])*(x-xj[j])+((pjPP[j+1]-pjPP[j])/(6.0*h))*(x-xj[j])*(x-xj[j])*(x-xj[j])
        holdValuesp.append(p)
        holdValuesx.append(x)
        holdValuesfx.append(f(x))

        print('{}   {}   {}'.format(x,p,f(x)))
        x += 0.1

    return holdValuesx, holdValuesp, holdValuesfx

def plot(x,y,fx):
    plt.plot(x,y)
    plt.plot(fx,y)
    plt.show()


if __name__ == '__main__':
    x, y, fx = main()
    plot(x,y,fx)