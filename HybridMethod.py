import math

def f(x):
    return (6435.0 * (x**8) - 12012.0 * (x**6) + 6930.0 * (x**4) - 1260.0 * (x ** 2) + 35) / 128.0
#   return x * x - 2.0 * x - 2.0


def fp(x):
    return (6435.0 * 8.0 * (x**7) - 12012.0 * 6.0 * (x**5) + 6930.0 * 4.0 * (x ** 3) - 1260.0 * 2.0 * x) / 128.0
#   return 2.0 * x - 2.0

def main():
    xL = float(input('Enter xL: '))
    xR = float(input('Enter xR: '))
    Tolerance = float(input('Enter tolerance: '))
    xOld = xL

    LT = (xOld - xL) * fp(xOld) - f(xOld)
    RT = (xOld - xR) * fp(xOld) - f(xOld)

    if (LT * RT) < 0.0:  # We do Newton-Raphson
        xNew = xOld - (f(xOld) / fp(xOld))
    else:  # We do Bisection
        xNew = (xR + xL) / 2.0

    Error = math.fabs((xNew-xOld)/xNew)

    numberOfIterations = 1

    while (Error > Tolerance):
        LT = (xOld - xL) * fp(xOld)-f(xOld)
        RT = (xOld - xR) * fp(xOld)-f(xOld)

        if (LT*RT) < 0.0:       # We do Newton-Raphson
            xNew = xOld - (f(xOld)/fp(xOld))
            print('Newton-Raphson i={} xNew={}'.format(numberOfIterations, xNew))
        else:                   # We do Bisection
            xNew = (xR+xL) / 2.0
            print('Bisection i={} xNew={}'.format(numberOfIterations, xNew))

        # change xR or xL
        if f(xL) * f(xNew) < 0.0:       # Root is between xL and xNew
            xR = xNew
        else:                           # Root is between xNew and xR
            xl = xNew

        Error = math.fabs((xNew-xOld)/xNew)
        xOld = xNew
        numberOfIterations += 1

    print('Root fount at {:.8f}'.format(xNew))
    print('Number of iterations {} '.format(numberOfIterations))

if __name__ == '__main__':
    main()